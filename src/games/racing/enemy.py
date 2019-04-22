import pygame

from src.games.racing.settings import Settings
from src.resources.racing_resources import RacingResources


class Enemy(pygame.sprite.Sprite):
    IMAGE = pygame.image.load(RacingResources.ENEMY_TEXTURE_PATH)

    def __init__(self, group_of_enemies, board, roadway):
        pygame.sprite.Sprite.__init__(self, group_of_enemies)
        self._roadway = roadway
        self._board = board
        self._car_y_pos = -1

        self._part_size = Settings.CAR_SIZE
        self.image = pygame.transform.scale(Enemy.IMAGE, self._part_size)
        self.rect = self.image.get_rect()
        self.rect.center = self._board.get_board_field_rect(self._roadway, 0).center
        self.rect = self.rect.move(0, -Settings.CAR_SIZE[1])  # initially moves car out of above board

    def _go_down(self):
        self._car_y_pos += 1
        self._remove_car_if_out_of_border()
        self.rect.center = self._board.get_board_field_rect(self._roadway, self._car_y_pos).center

    def _remove_car_if_out_of_border(self):
        if self._car_y_pos >= self._board.get_amount_of_fields_vertically() - 1:
            self.kill()

    def update(self):
        self._go_down()
