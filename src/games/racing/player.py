import pygame

from src.resources.layout_rsc import LayoutRsc


class Player:
    LEFT_ROADWAY = 0
    RIGHT_ROADWAY = 1

    IMAGE = pygame.image.load(LayoutRsc.TEXTURES_PATH + 'racing/player.png')
    def __init__(self, board, roadway_width):
        self._part_size = (int(roadway_width*0.7), 70)
        self.image = pygame.transform.scale(Player.IMAGE, self._part_size)
        self.rect = self.image.get_rect()

        self._board = board
        self._car_y_pos = self._board.get_amount_of_fields_vertically()-3
        self.rect.center = self._board.get_board_field_rect(Player.LEFT_ROADWAY, self._car_y_pos).center

    def render(self, window):
        window.blit(self.image, self.rect)

    def update(self):
        pass

    def take_roadway(self, roadway):
        if roadway == "left":
            self.rect.center = self._board.get_board_field_rect(Player.LEFT_ROADWAY, self._car_y_pos).center
        elif roadway == "right":
            self.rect.center = self._board.get_board_field_rect(Player.RIGHT_ROADWAY, self._car_y_pos).center
        else:
            raise Exception("invalid roadway")


