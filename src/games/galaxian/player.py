from src.helpers.dotdict import *
from src.games.galaxian.projectile import *
import pygame


class Player(pygame.sprite.Sprite):
    WIDTH = 40
    HEIGHT = 45
    TEXTURE = pygame.transform.scale(pygame.image.load(GalaxianRsc.PLAYER_TEXTURE_PATH), (WIDTH, HEIGHT))
    TRANSPARENT_TEXTURE = pygame.transform.scale(pygame.image.load(GalaxianRsc.PLAYER_TEXTURE_PATH), (WIDTH, HEIGHT))
    TRANSPARENT_TEXTURE.fill((0, 0, 0, 0))
    RESPAWN_TIME_SEC = 2
    LAUNCH_COOLDOWN_SEC = 0.35
    SECOND = 1000
    BLINK_TIME = 0.4 * SECOND

    def __init__(self, x, y, projectiles, is_sound_on):
        pygame.sprite.Sprite.__init__(self)
        self.image = Player.TEXTURE
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self._is_sound_on = is_sound_on
        self._initial_x = x
        self._initial_y = y
        self._projectiles = projectiles
        self._is_moving = DotDict({"left": False, "right": False})
        self._launch_projectile = False
        self._is_respawning = False
        self._respawn_elapsed_time = 0
        self._launch_elapsed_time = 0

    def move_left(self):
        self._is_moving.left = True

    def move_right(self):
        self._is_moving.right = True

    def launch_projectile(self):
        self._launch_projectile = True

    def update(self, delta_time):
        self._launch_elapsed_time += delta_time
        if self._is_respawning:
            self._respawn_elapsed_time += delta_time
            self.rect.center = (self._initial_x, self._initial_y)
            if self._respawn_elapsed_time * Player.SECOND % Player.BLINK_TIME < Player.BLINK_TIME / 2:
                self.image = Player.TRANSPARENT_TEXTURE
            else:
                self.image = Player.TEXTURE
            if self._respawn_elapsed_time > Player.RESPAWN_TIME_SEC:
                self.image = Player.TEXTURE
                self._is_respawning = False
                self._respawn_elapsed_time = 0
        else:
            if self._is_moving.left:
                if self.rect.x > 0:
                    self.rect.x -= Player.WIDTH
                self._is_moving.left = False
            elif self._is_moving.right:
                if self.rect.x < LayoutRsc.GAME_AREA_WIDTH - Player.WIDTH:
                    self.rect.x += Player.WIDTH
                self._is_moving.right = False
            if self._launch_projectile:
                if self._launch_elapsed_time > Player.LAUNCH_COOLDOWN_SEC:
                    self._projectiles.add(Projectile(self.rect.center[0], self.rect.center[1]))
                    self._play_sound_if_needed(GalaxianRsc.PROJECTILE_LAUNCH)
                    self._launch_elapsed_time = 0
                self._launch_projectile = False

    def respawn(self):
        self._is_respawning = True

    def _play_sound_if_needed(self, sound):
        if self._is_sound_on:
            sound.play()
