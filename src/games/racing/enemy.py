import pygame

from src.resources.layout_rsc import LayoutRsc


class Enemy(pygame.sprite.Sprite):

    IMAGE = pygame.image.load(LayoutRsc.TEXTURES_PATH + 'racing/enemy.png')

    def __init__(self, group_of_enemies, board, roadway_width, initial_roadway):
        pygame.sprite.Sprite.__init__(self, group_of_enemies)
        self._part_size = (int(roadway_width * 0.7), 70)
        self.image = pygame.transform.scale(Enemy.IMAGE, self._part_size)
        self.rect = self.image.get_rect()
        self._roadway = initial_roadway

        self._board = board
        self._car_y_pos = 0
        self.rect.center = self._board.get_board_field_rect(self._roadway, self._car_y_pos).center



    def _go_down(self):
        self._car_y_pos += 1
        self.rect.center = self._board.get_board_field_rect(self._roadway, self._car_y_pos).center

    def update(self):
        self._go_down()
        if self._car_y_pos >= self._board.get_amount_of_fields_vertically():
            self.kill()
