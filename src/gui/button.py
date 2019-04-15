import pygame.draw
from src.gui.indented_rect import *
from src.resources.layout_rsc import *


class Button(IndentedRect):
    def __init__(self, pos_x, pos_y, width, height, id, is_disabled=False):
        IndentedRect.__init__(self, pos_x, pos_y, width, height)
        self._id = id
        self._is_disabled = is_disabled

    def get_id(self):
        return self._id

    def is_disabled(self):
        return self._is_disabled

    def draw_regular(self, window):
        super().draw(window, LayoutRsc.ITEM_REGULAR_BG_COLOR)

    def draw_highlighted(self, window):
        if self._is_disabled:
            self.draw_regular(window)
        else:
            super().draw(window, LayoutRsc.ITEM_HIGHLIGHTED_BG_COLOR)
