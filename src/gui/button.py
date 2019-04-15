from src.gui.clipped_rect import *


class Button(ClippedRect):
    def __init__(self, pos_x, pos_y, width, height, id, is_disabled=False):
        ClippedRect.__init__(self, pos_x, pos_y, width, height)
        self._id = id
        self._is_disabled = is_disabled

    def get_id(self):
        return self._id

    def is_disabled(self):
        return self._is_disabled

    def draw_focused(self, window):
        super().draw(window, LayoutRsc.ITEM_REGULAR_BG_COLOR)

    def draw_not_focused(self, window):
        if self._is_disabled:
            self.draw_focused(window)
        else:
            super().draw(window, LayoutRsc.ITEM_HIGHLIGHTED_BG_COLOR)
