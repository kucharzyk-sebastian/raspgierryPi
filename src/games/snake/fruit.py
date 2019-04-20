import pygame
from src.resources.snake_game_resources import SnakeGameResources


class Fruit(pygame.sprite.Sprite):
    def __init__(self, board):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(SnakeGameResources.FRUIT_TEXTURE_PATH), board.get_field_size())
        self.rect = self.image.get_rect()
