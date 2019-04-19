from random import randrange

import pygame

from src.resources.layout_rsc import LayoutRsc


class Fruit(pygame.sprite.Sprite):
    TEXTURE_PATH = LayoutRsc.TEXTURES_PATH + '/snake/fruit.png'

    def __init__(self, board):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(Fruit.TEXTURE_PATH), board.get_field_size())
        self.rect = self.image.get_rect()


class Board():

    def __init__(self, width, height, fields_horizontally, fields_vertically):
        self._fields_horizontally = fields_horizontally
        self._fields_vertically = fields_vertically
        self._field_width = int(width/fields_horizontally)
        self._field_height = int(height/fields_vertically)
        self._grid = [[pygame.Rect(x*self._field_width , y*self._field_height, self._field_width, self._field_height)
                         for y in range(fields_vertically)]
                             for x in range(fields_horizontally)]

        self._fruit = Fruit(self)
        self._fruit.rect.center = self.get_rect(0,0).center # TODO jagros: put it randomly


    def get_fruit(self):
        return self._fruit

    def get_rect(self, x, y):
        return self._grid[x][y]

    def get_field_size(self):
        return (self._field_width, self._field_height)

    def is_on_fruit_pos(self, rect):
        return self._fruit.rect.colliderect(rect)

    def remove_old_fruit_and_put_new(self, snake):
        while True:
            new_fruit_x_pos = randrange(self._fields_horizontally)
            new_fruit_y_pos = randrange(self._fields_vertically)
            new_fruit_rect = pygame.Rect(new_fruit_x_pos, new_fruit_y_pos, self._field_width, self._field_height)
            new_fruit_sprite = pygame.sprite.Sprite()
            new_fruit_sprite.rect = new_fruit_rect
            if(pygame.sprite.spritecollide(new_fruit_sprite, snake.get_occupied_points()) == None):
                break;

    def get_middle(self):
        return self._grid[int(self._fields_horizontally/2)][int(self._fields_vertically/2)]