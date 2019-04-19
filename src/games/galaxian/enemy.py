from src.resources.galaxian_resources import *
import pygame


class Enemy(pygame.sprite.Sprite):
    WIDTH = 40
    HEIGHT = 35
    TEXTURE = pygame.transform.scale(pygame.image.load(GalaxianRsc.ENEMY_TEXTURE_PATH), (WIDTH, HEIGHT))
    SPECIAL_TEXTURE = pygame.transform.scale(pygame.image.load(GalaxianRsc.SPECIAL_ENEMY_TEXTURE_PATH), (WIDTH, HEIGHT))

    def __init__(self, x, y, is_special=False):
        pygame.sprite.Sprite.__init__(self)
        self.image = Enemy.SPECIAL_TEXTURE if is_special else Enemy.TEXTURE
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self._is_special = is_special
        self._is_moving_down = False

    def is_special(self):
        return self._is_special

    def go_down(self):
        self._is_moving_down = True

    def update(self, delta_time):
        if self._is_moving_down:
            self.rect.y += Enemy.HEIGHT
            self._is_moving_down = False
