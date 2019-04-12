import pygame.draw
from src.resources.layout_rsc import *


class Button:
    def __init__(self, pos_x, pos_y, width, height, type, is_disabled=False):
        self._x = pos_x
        self._y = pos_y
        self._width = width
        self._height = height
        self._type = type
        self._is_disabled = is_disabled

    def get_pos_x(self):
        return self._x

    def get_pos_y(self):
        return self._y

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_type(self):
        return self._type

    def is_disabled(self):
        return self._is_disabled

    def draw_regular(self, window):
        self.draw(window, LayoutRsc.regular_bg_color)

    def draw_highlighted(self, window):
        if self._is_disabled:
            self.draw_regular(window)
        else:
            self.draw(window, LayoutRsc.highlighted_bg_color)

    def draw_shape(self, window, bg_color):
        pygame.draw.rect(window, bg_color, (self._x, self._y, self._width, self._height))

        pygame.draw.line(window, LayoutRsc.line_bg_color, (self._x + LayoutRsc.line_indent - 1, self._y - 1), (self._x + self._width - LayoutRsc.line_indent - 1, self._y - 1), LayoutRsc.line_bg_thickness)
        pygame.draw.line(window, LayoutRsc.line_color, (self._x + LayoutRsc.line_indent, self._y), (self._x + self._width - LayoutRsc.line_indent, self._y), LayoutRsc.line_thickness)

        pygame.draw.line(window, LayoutRsc.line_bg_color, (self._x - 1, self._y + LayoutRsc.line_indent - 1), (self._x - 1, self._y + self._height - LayoutRsc.line_indent - 1), LayoutRsc.line_bg_thickness)
        pygame.draw.line(window, LayoutRsc.line_color, (self._x, self._y + LayoutRsc.line_indent), (self._x, self._y + self._height - LayoutRsc.line_indent), LayoutRsc.line_thickness)

        pygame.draw.line(window, LayoutRsc.line_bg_color, (self._x + self._width - 1, self._y + LayoutRsc.line_indent - 1), (self._x + self._width - 1, self._y + self._height - LayoutRsc.line_indent - 1), LayoutRsc.line_bg_thickness)
        pygame.draw.line(window, LayoutRsc.line_color, (self._x + self._width, self._y + LayoutRsc.line_indent), (self._x + self._width, self._y + self._height - LayoutRsc.line_indent), LayoutRsc.line_thickness)

        pygame.draw.line(window, LayoutRsc.line_bg_color, (self._x + LayoutRsc.line_indent - 1, self._y + self._height - 1), (self._x + self._width - LayoutRsc.line_indent - 1, self._y + self._height - 1), LayoutRsc.line_bg_thickness)
        pygame.draw.line(window, LayoutRsc.line_color, (self._x + LayoutRsc.line_indent, self._y + self._height), (self._x + self._width - LayoutRsc.line_indent, self._y + self._height), LayoutRsc.line_thickness)

    def draw(self, window, bg_color):
        self.draw_shape(window, bg_color)
