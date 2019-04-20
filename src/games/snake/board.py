from random import randrange
import pygame
from src.games.snake.fruit import Fruit


class Board:
    def __init__(self, width, height, fields_horizontally, fields_vertically):
        self._fields_horizontally = fields_horizontally
        self._fields_vertically = fields_vertically

        self._field_width = int(width / fields_horizontally)
        self._field_height = int(height / fields_vertically)
        self._grid = [[pygame.Rect(x * self._field_width, y * self._field_height, self._field_width, self._field_height)
                       for y in range(fields_vertically)]
                      for x in range(fields_horizontally)]

        self._fruit = Fruit(self)
        self._fruit.rect.center = self.get_middle().center

    def get_middle(self):
        return self._grid[int(self._fields_horizontally / 2)][int(self._fields_vertically / 2)]

    def get_fruit(self):
        return self._fruit

    def get_board_field_rect(self, x, y):
        return self._grid[x % self._fields_horizontally][y % self._fields_vertically]

    def get_field_size(self):
        return self._field_width, self._field_height

    def is_on_fruit_pos(self, rect):
        return self._fruit.rect.colliderect(rect)

    def remove_old_fruit_and_put_new(self, snake):
        self._fruit.rect = None

        while self._fruit.rect is None:
            new_fruit = pygame.sprite.Sprite()
            new_fruit.rect = self.get_board_field_rect(randrange(self._fields_horizontally),
                                                       randrange(self._fields_vertically))
            if pygame.sprite.spritecollideany(new_fruit, snake.get_occupied_points()) is None:
                self._fruit.rect = new_fruit.rect
