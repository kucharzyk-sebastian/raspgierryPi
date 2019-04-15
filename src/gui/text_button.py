from src.resources.font_rsc import *
from src.helpers.text import *
from src.gui.button import *


class TextButton(Button):
    def __init__(self, pos_x, pos_y, width, height, text, id, is_disabled=False):
        Button.__init__(self, pos_x, pos_y, width, height, id, is_disabled)
        self._text = text

    def get_text(self):
        return self._text

    def draw_regular(self, window):
        super().draw_regular(window)
        self._draw_text(window)

    def draw_highlighted(self, window):
        super().draw_highlighted(window)
        self._draw_text(window)

    def _draw_text(self, window):
        if isinstance(self._text, list):
            line_size = FontRsc.CONTENT_FONT_SMALL.get_linesize()
            current_height = self._y + line_size
            for line in self._text:
                Text.render_centered_text(surface=window,
                                          center_x=self._x + self._width / 2,
                                          center_y=current_height,
                                          font=FontRsc.CONTENT_FONT_SMALL,
                                          text=line,
                                          color=FontRsc.CONTENT_FONT_COLOR)
                current_height += line_size + 0.25 * line_size
        else:
            Text.render_centered_text(surface=window,
                                      center_x=self._x + self._width / 2,
                                      center_y=self._y + self._height / 2 + self._height * 0.08,
                                      font=FontRsc.CONTENT_FONT_REGULAR,
                                      text=self._text,
                                      color=FontRsc.CONTENT_FONT_COLOR)
