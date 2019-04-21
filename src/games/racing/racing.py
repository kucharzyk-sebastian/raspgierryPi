import pygame

from src.games.game import *
from src.resources.layout_rsc import LayoutRsc
from pygame import *
class Board():

    FIELDS_OCCUPIED_BY_CAR = 4
    def __init__(self, width, height, fields_horizontally, fields_vertically):
        self._fields_horizontally = fields_horizontally
        self._fields_vertically = fields_vertically

        self._field_width = int(width / fields_horizontally)
        self._field_height = int(height / fields_vertically)
        self._grid = [[pygame.Rect(x * self._field_width, y * self._field_height, self._field_width, self._field_height)
                        for y in range(fields_vertically + Board.FIELDS_OCCUPIED_BY_CAR)] #additional fields for buffor(car is generated but not visible yet)
                            for x in range(fields_horizontally)]


    def get_board_field_rect(self, x, y):
        return self._grid[x][y]

    def get_amount_of_fields_horizontally(self):
        return self._fields_horizontally

    def get_amount_of_fields_vertically(self):
        return self._fields_vertically

    def get_field_size(self):
        return self._field_width, self._field_height





class Player:
    LEFT_ROADWAY = 0
    RIGHT_ROADWAY = 1

    IMAGE = pygame.image.load(LayoutRsc.TEXTURES_PATH + 'racing/player.png')
    def __init__(self, board, roadway_width):
        self._part_size = (int(roadway_width*0.7), 70)
        self._image = pygame.transform.scale(Player.IMAGE, self._part_size)
        self._rect = self._image.get_rect()

        self._board = board
        self._car_y_pos = self._board.get_amount_of_fields_vertically()-3
        self._rect.center = self._board.get_board_field_rect(Player.LEFT_ROADWAY, self._car_y_pos).center

    def render(self, window):
        window.blit(self._image, self._rect)

    def update(self, delta_time):
        pass

    def take_roadway(self, roadway):
        if roadway == "left":
            self._rect.center = self._board.get_board_field_rect(Player.LEFT_ROADWAY, self._car_y_pos).center
        elif roadway == "right":
            self._rect.center = self._board.get_board_field_rect(Player.RIGHT_ROADWAY, self._car_y_pos).center
        else:
            raise Exception("invalid roadway")


class Racing(Game):
    def __init__(self, level, is_sound_on):
        Game.__init__(self, level, is_sound_on)
        self._board = Board(LayoutRsc.GAME_AREA_WIDTH, LayoutRsc.GAME_AREA_HEIGHT, 2, 20)
        self._roadway_width = LayoutRsc.GAME_AREA_WIDTH/2
        self._player = Player(self._board, self._roadway_width)

    def process_events(self, joystick):
        for event in pygame.event.get():
            joystick.process_event(event)

            if event.type in {JOYBUTTONUP, JOYBUTTONDOWN, JOYAXISMOTION}:
                if joystick.is_arrow_leftdir_pressed():
                    self._player.take_roadway("left")
                if joystick.is_arrow_rightdir_pressed():
                    self._player.take_roadway("right")

    def update(self, delta_time):
        self._player.update(delta_time)

    def render(self, window):
        window.fill(LayoutRsc.WINDOW_COLOR)
        self._player.render(window)


    def is_running(self):
        return self._is_running

    def get_points(self):
        return self._points

    def get_lives(self):
        return self._lives
