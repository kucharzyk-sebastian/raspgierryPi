import pygame


class Board():
    FIELDS_OCCUPIED_BY_CAR = 4  # todo jagros calculate somehow

    def __init__(self, width, height, fields_horizontally, fields_vertically):
        self._fields_horizontally = fields_horizontally
        self._fields_vertically = fields_vertically + Board.FIELDS_OCCUPIED_BY_CAR  # additional so that car could smoothly disapear from board

        self._field_width = int(width / fields_horizontally)
        self._field_height = int(height / fields_vertically)
        self._grid = [[pygame.Rect(x * self._field_width, y * self._field_height, self._field_width, self._field_height)
                       for y in range(self._fields_vertically)]
                      for x in range(self._fields_horizontally)]

    def get_board_field_rect(self, x, y):
        return self._grid[x][y]

    def get_amount_of_fields_horizontally(self):
        return self._fields_horizontally

    def get_amount_of_fields_vertically(self):
        return self._fields_vertically

    def get_field_size(self):
        return self._field_width, self._field_height
