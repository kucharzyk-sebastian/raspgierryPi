import pygame
from src.resources.snake_game_resources import SnakeGameResources


class SnakePart(pygame.sprite.Sprite):

    IMAGE = pygame.image.load(SnakeGameResources.SNAKE_PART_TEXTURE_PATH)

    def __init__(self, owner, board, pos_center=None):
        pygame.sprite.Sprite.__init__(self, owner)
        self._part_size = board.get_field_size()
        self.image = pygame.transform.scale(SnakePart.IMAGE, self._part_size)
        self.rect = self.image.get_rect()
        if pos_center:
            self.rect.center = pos_center
        else:
            self.rect.center = board.get_middle().center
        self._group = owner
        self._alive_cycles_left = len(self._group)

    def update(self):
        self._alive_cycles_left -= 1
        if self._alive_cycles_left <= 0:
            self.kill()

    def increase_lifetime(self):
        self._alive_cycles_left += 1
