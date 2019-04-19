from src.games.game import *
from src.controls.joystick import *
from src.settings import GameLevel
from src.games.galaxian.player import *
from src.games.galaxian.enemy import *
import pygame
import sys
import random


class Galaxian(Game):
    SPEEDS = {GameLevel.Easy: 10, GameLevel.Medium: 20, GameLevel.Hard: 40}

    def __init__(self, level, is_sound_on):
        Game.__init__(self, level, is_sound_on)
        self._points = 0
        self._lives = 3
        self._enemies = pygame.sprite.Group()
        self._projectiles = pygame.sprite.Group()
        self._player = Player(x=LayoutRsc.GAME_AREA_WIDTH / 2,
                              y=LayoutRsc.GAME_AREA_HEIGHT - Player.HEIGHT/2,
                              projectiles=self._projectiles,
                              is_sound_on=is_sound_on)
        self.enemy_speed = Galaxian.SPEEDS[level]
        self._add_row_of_enemies()
        self._first_enemies_row_y = 0

    def _add_row_of_enemies(self):
        enemies_in_row = 7
        enemies = []
        special_enemy_idx = random.randrange(0, enemies_in_row)
        for i in range(enemies_in_row):
            if i == special_enemy_idx:
                enemies.append(Enemy(Enemy.WIDTH/2 + i*Enemy.WIDTH, Enemy.HEIGHT / 2, True))
            else:
                enemies.append(Enemy(Enemy.WIDTH/2 + i*Enemy.WIDTH, Enemy.HEIGHT / 2))
        self._enemies.add(enemies)
        self._play_sound_if_needed(GalaxianRsc.ENEMY_GETS_CLOSER)

    def update(self, delta_time):
        self._player.update(delta_time)
        self._enemies.update(delta_time)
        self._projectiles.update(delta_time)
        self._update_enemies_rows(delta_time)
        self._collide_enemies_with_projectiles()
        self._destroy_outrange_projectiles()
        self._collide_enemies_with_player()

    def _update_enemies_rows(self, delta_time):
        self._first_enemies_row_y += self.enemy_speed * delta_time
        if self._first_enemies_row_y >= Enemy.HEIGHT:
            for enemy in self._enemies:
                enemy.go_down()
            self._add_row_of_enemies()
            self._first_enemies_row_y = 0

    def _collide_enemies_with_projectiles(self):
        for enemy in pygame.sprite.groupcollide(self._enemies, self._projectiles, True, True):
            if enemy.is_special():
                self._points += 3
                self._play_sound_if_needed(GalaxianRsc.SPECIAL_ENEMY_DEATH)
            else:
                self._points += 1
                self._play_sound_if_needed(GalaxianRsc.ENEMY_DEATH)

    def _destroy_outrange_projectiles(self):
        for p in self._projectiles:
            if p.rect.center[1] < 0:
                p.kill()

    def _collide_enemies_with_player(self):
        for enemy in self._enemies:
            if enemy.rect.midbottom[1] > LayoutRsc.GAME_AREA_HEIGHT - Player.HEIGHT:
                self._lives -= 1
                if self._lives == 0:
                    self._is_running = False
                else:
                    self._enemies.empty()
                    self._projectiles.empty()
                    self._play_sound_if_needed(GalaxianRsc.PLAYER_DEATH)
                    self._player.respawn()
                break

    def render(self, window):
        window.fill(LayoutRsc.WINDOW_COLOR)
        self._enemies.draw(window)
        self._projectiles.draw(window)
        window.blit(self._player.image, self._player.rect)

    def process_events(self, joystick):
        for event in pygame.event.get():
            if event.type in {JOYBUTTONUP, JOYBUTTONDOWN, JOYAXISMOTION}:
                joystick.process_event(event)
                if joystick.is_a_pressed():
                    self._player.launch_projectile()
                if joystick.is_arrow_rightdir_pressed():
                    self._player.move_right()
                if joystick.is_arrow_leftdir_pressed():
                    self._player.move_left()

    def get_points(self):
        return self._points

    def get_lives(self):
        return self._lives

    def _play_sound_if_needed(self, sound):
        if self._is_sound_on:
            sound.play()
