import pygame.draw
from enum import Enum
from src.gui.button import *
from src.resources.font_rsc import *
from src.resources.layout_rsc import *
from src.helpers.text import *


class TextButtonWidth(Enum):
    NARROW = 0
    WIDE = 1


class TextButtonHeight(Enum):
    REGULAR = 50


class TextButton(Button):
    height = 50

    def __init__(self, pos_x, pos_y, width: TextButtonWidth, height=TextButtonHeight.REGULAR.value, text="", type=None, is_disabled=False):
        self._height = height
        self._size = width
        if width == TextButtonWidth.WIDE:
            width = LayoutRsc.usable_area_width
        elif width == TextButtonWidth.NARROW:
            width = LayoutRsc.usable_area_width / 2 - 5
        else:
            raise NotImplementedError
        Button.__init__(self, pos_x, pos_y, width, self._height, type, is_disabled)
        self._text = text

    def get_size(self):
        return self._size

    def get_text(self):
        return self._text

    def draw(self, window, bg_color):
        self.draw_shape(window, bg_color)
        if isinstance(self._text, list):
            line_size = FontRsc.paragraph_font.get_linesize()
            current_height = self._y + line_size
            for line in self._text:
                Text.render_centered_text(window, self._x + self._width / 2, current_height, FontRsc.paragraph_font, line,
                                          LayoutRsc.line_color)
                current_height += line_size + 0.25 * line_size
        else:
            Text.render_centered_text(window, self._x + self._width / 2, self._y + self._height / 2 + self._height * 0.08, FontRsc.content_font, self._text, LayoutRsc.line_color)
