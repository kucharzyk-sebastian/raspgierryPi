import pygame.draw
from src.gui.button import *
from src.resources.font_rsc import *
from src.resources.layout_rsc import *
from src.helpers.text import *


class TextButton(Button):
    def __init__(self, pos_x, pos_y, width, height, text, id, is_disabled=False):
        Button.__init__(self, pos_x, pos_y, width, height, id, is_disabled)
        self._text = text

    def get_text(self):
        return self._text

    def draw(self, window, bg_color):
        self.draw_shape(window, bg_color)
        if isinstance(self._text, list):
            line_size = FontRsc.CONTENT_FONT_SMALL.get_linesize()
            current_height = self._y + line_size
            for line in self._text:
                Text.render_centered_text(window, self._x + self._width / 2, current_height, FontRsc.CONTENT_FONT_SMALL, line, FontRsc.CONTENT_FONT_COLOR)
                current_height += line_size + 0.25 * line_size
        else:
            Text.render_centered_text(window, self._x + self._width / 2, self._y + self._height / 2 + self._height * 0.08, FontRsc.CONTENT_FONT_REGULAR, self._text, FontRsc.CONTENT_FONT_COLOR)
