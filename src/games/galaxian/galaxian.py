from src.resources.layout_rsc import *
from src.resources.sound_rsc import *
from src.games.game import *
from src.controls.joystick import *
import pygame
import sys


class Enemy(pygame.sprite.Sprite):
    TEXTURE_PATH = LayoutRsc.TEXTURES_PATH + '/galaxian/enemy_1.png'
    TEXTURE_SIZE = (40, 28)
    SPEED = 4

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self._x = x
        self._y = y
        self.image = pygame.transform.scale(pygame.image.load(Enemy.TEXTURE_PATH), Enemy.TEXTURE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self, delta_time):
        self._y += Enemy.SPEED * delta_time
        if (self._y - self.rect.y) > Enemy.TEXTURE_SIZE[1]:
            self.rect.y = self._y


class Projectile(pygame.sprite.Sprite):
    TEXTURE_PATH = LayoutRsc.TEXTURES_PATH + '/galaxian/projectile.png'
    TEXTURE_SIZE = (8, 8)
    SPEED = 40

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self._x = x
        self._y = y
        self.image = pygame.transform.scale(pygame.image.load(Projectile.TEXTURE_PATH), Projectile.TEXTURE_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, delta_time):
        self._y -= Projectile.SPEED * delta_time
        if (self.rect.y - self._y) > Projectile.SPEED:
            self.rect.y = self._y


class Player(pygame.sprite.Sprite):
    TEXTURE_PATH = LayoutRsc.TEXTURES_PATH + '/galaxian/ship.png'
    TEXTURE_SIZE = (40, 45)
    INNER_MARGIN = 5
    SPEED = 40

    def __init__(self, projectiles, is_sound_on):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(Player.TEXTURE_PATH), Player.TEXTURE_SIZE)
        self.rect = self.image.get_rect()
        self._is_moving = DotDict({"left": False, "right": False})
        self._launch_projectile = False
        self._sprites = projectiles
        self._is_sound_on = is_sound_on

    def move_left(self):
        self._is_moving.left = True

    def move_right(self):
        self._is_moving.right = True

    def launch_projectile(self):
        self._launch_projectile = True

    def update(self, delta_time):
        if self._is_moving.left:
            if self.rect.x > 0:
                self.rect.x -= Player.SPEED
            self._is_moving.left = False
        elif self._is_moving.right:
            if self.rect.x < LayoutRsc.GAME_AREA_WIDTH - Player.TEXTURE_SIZE[0]:
                self.rect.x += Player.SPEED
            self._is_moving.right = False

        if self._launch_projectile:
            self._sprites.add(Projectile(self.rect.center[0], self.rect.center[1]))
            self.play_sound_if_needed(SoundRsc.projectile_launch)
            self._launch_projectile = False

    def play_sound_if_needed(self, sound):
        if self._is_sound_on:
            sound.play()


class Galaxian(Game):
    def __init__(self, level, is_sound_on):
        Game.__init__(self, level, is_sound_on)
        self.points = 0
        self.lives = 3
        self.enemies = pygame.sprite.Group()
        self.projectiles = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self._player = Player(self.projectiles, is_sound_on)
        self.players.add(self._player)
        self._player.rect.center = (LayoutRsc.GAME_AREA_WIDTH / 2, LayoutRsc.GAME_AREA_HEIGHT - Player.TEXTURE_SIZE[1]/2)

        enemies = [Enemy(0, 0)]
        while enemies[-1].rect.topleft[0] + Enemy.TEXTURE_SIZE[0] < LayoutRsc.GAME_AREA_WIDTH:
            enemies.append(Enemy(enemies[-1].rect.topleft[0] + Enemy.TEXTURE_SIZE[0], enemies[-1].rect.topleft[1]))
        self.enemies.add(enemies)
        enemies = []

    def update(self, delta_time):
        res = pygame.sprite.groupcollide(self.enemies, self.projectiles, True, True)
        for i in range(len(res)):
            self.play_sound_if_needed(SoundRsc.enemy_death)
            self.points += 10

        self.enemies.update(delta_time)
        self.projectiles.update(delta_time)
        self.players.update(delta_time)
        for p in self.projectiles:
            if p.rect.center[1] < 0:
                p.kill()

        for e in self.enemies:
            if e.rect.midbottom[1] >= LayoutRsc.GAME_AREA_HEIGHT:
                pass
                #self._is_running = False

    def render(self, window):
        window.fill(LayoutRsc.WINDOW_COLOR)
        self.enemies.draw(window)
        self.projectiles.draw(window)
        self.players.draw(window)

    def process_events(self, joystick):
        for event in pygame.event.get():
            # TODO sk: remove these lines when game ready
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                sys.exit(0)

            if event.type in {JOYBUTTONUP, JOYBUTTONDOWN, JOYAXISMOTION}:
                joystick.process_event(event)
                if joystick.is_a_pressed():
                    self._player.launch_projectile()
                if joystick.is_arrow_rightdir_pressed():
                    self._player.move_right()
                if joystick.is_arrow_leftdir_pressed():
                    self._player.move_left()
                if joystick.is_b_pressed():
                    sys.exit(0)

    def get_points(self):
        return self.points

    def get_lives(self):
        return self.lives

    def play_sound_if_needed(self, sound):
        if self._is_sound_on:
            sound.play()
