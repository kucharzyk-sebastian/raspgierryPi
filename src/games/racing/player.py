import pygame

from src.games.racing.settings import Settings
from src.resources.racing_resources import RacingResources


class Player:
    LEFT_ROADWAY = 0
    RIGHT_ROADWAY = 1

    IMAGE = pygame.transform.scale(pygame.image.load(RacingResources.PLAYER_TEXTURE_PATH), Settings.CAR_SIZE)

    def __init__(self, board):
        self.image = Player.IMAGE
        self.rect = self.image.get_rect()

        self._board = board
        self._car_y_pos = self._board.get_amount_of_fields_vertically() - 2 * Settings.BUFFER_FIELDS_OUT_OF_BOARD
        self.rect.center = self._board.get_board_field_rect(Player.LEFT_ROADWAY, self._car_y_pos).center
        self._occupied_roadway = "left"

    def render(self, window):
        window.blit(self.image, self.rect)

    def update(self):
        if self._occupied_roadway == "left":
            self.rect.center = self._board.get_board_field_rect(Player.LEFT_ROADWAY, self._car_y_pos).center
        elif self._occupied_roadway == "right":
            self.rect.center = self._board.get_board_field_rect(Player.RIGHT_ROADWAY, self._car_y_pos).center

    def take_roadway(self, roadway):
        allowed_roadways = ["left", "right"]
        if roadway not in allowed_roadways:
            raise Exception("invalid roadway")

        self._occupied_roadway = roadway
