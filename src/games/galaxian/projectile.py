from src.resources.galaxian_resources import *
import pygame


class Projectile(pygame.sprite.Sprite):
    WIDTH = 8
    HEIGHT = 8
    SPEED = 128
    TEXTURE = pygame.transform.scale(pygame.image.load(GalaxianRsc.PROJECTILE_TEXTURE_PATH), (WIDTH, HEIGHT))

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = Projectile.TEXTURE
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self._absolute_y = y

    def update(self, delta_time):
        self._absolute_y -= Projectile.SPEED * delta_time
        if (self.rect.y - self._absolute_y) > Projectile.HEIGHT:
            self.rect.y = self._absolute_y
