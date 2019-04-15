import pygame.draw
from src.resources.layout_rsc import *


class ClippedRect:
    def __init__(self, pos_x, pos_y, width, height):
        self._x = pos_x
        self._y = pos_y
        self._width = width
        self._height = height

    def get_pos_x(self):
        return self._x

    def get_pos_y(self):
        return self._y

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def draw(self, window, bg_color):
        pygame.draw.rect(window, bg_color, (self._x, self._y, self._width, self._height))

        pygame.draw.line(window,
                         LayoutRsc.LINE_SHADOW_COLOR,
                         (self._x + LayoutRsc.CORNER_INDENT - 1, self._y - 1),
                         (self._x + self._width - LayoutRsc.CORNER_INDENT - 1, self._y - 1),
                         LayoutRsc.LINE_SHADOW_THICKNESS)

        pygame.draw.line(window,
                         LayoutRsc.LINE_COLOR,
                         (self._x + LayoutRsc.CORNER_INDENT, self._y),
                         (self._x + self._width - LayoutRsc.CORNER_INDENT, self._y),
                         LayoutRsc.LINE_THICKNESS)

        pygame.draw.line(window,
                         LayoutRsc.LINE_SHADOW_COLOR,
                         (self._x - 1, self._y + LayoutRsc.CORNER_INDENT - 1),
                         (self._x - 1, self._y + self._height - LayoutRsc.CORNER_INDENT - 1),
                         LayoutRsc.LINE_SHADOW_THICKNESS)

        pygame.draw.line(window,
                         LayoutRsc.LINE_COLOR,
                         (self._x, self._y + LayoutRsc.CORNER_INDENT),
                         (self._x, self._y + self._height - LayoutRsc.CORNER_INDENT),
                         LayoutRsc.LINE_THICKNESS)

        pygame.draw.line(window,
                         LayoutRsc.LINE_SHADOW_COLOR,
                         (self._x + self._width - 1, self._y + LayoutRsc.CORNER_INDENT - 1),
                         (self._x + self._width - 1, self._y + self._height - LayoutRsc.CORNER_INDENT - 1),
                         LayoutRsc.LINE_SHADOW_THICKNESS)

        pygame.draw.line(window,
                         LayoutRsc.LINE_COLOR,
                         (self._x + self._width, self._y + LayoutRsc.CORNER_INDENT),
                         (self._x + self._width, self._y + self._height - LayoutRsc.CORNER_INDENT),
                         LayoutRsc.LINE_THICKNESS)

        pygame.draw.line(window,
                         LayoutRsc.LINE_SHADOW_COLOR,
                         (self._x + LayoutRsc.CORNER_INDENT - 1, self._y + self._height - 1),
                         (self._x + self._width - LayoutRsc.CORNER_INDENT - 1, self._y + self._height - 1),
                         LayoutRsc.LINE_SHADOW_THICKNESS)

        pygame.draw.line(window,
                         LayoutRsc.LINE_COLOR,
                         (self._x + LayoutRsc.CORNER_INDENT, self._y + self._height),
                         (self._x + self._width - LayoutRsc.CORNER_INDENT, self._y + self._height),
                         LayoutRsc.LINE_THICKNESS)
