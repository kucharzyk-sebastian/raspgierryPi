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

    def update(self, delta_time):
        self.rect.y -= Projectile.SPEED * delta_time
