from enum import Enum
from src.gui.text_button import *
from src.gui.multi_choice_button import *


class ButtonType(Enum):
    TEXT_NARROW = 0
    TEXT_WIDE = 1
    MULTI_CHOICE_SHORT = 2
    MULTI_CHOICE_LONG = 3
    TEXT_AREA = 4


class Page:
    HEADER_HEIGHT = 100
    MARGIN_LEFT = 40
    VERTICAL_SPACE = 20
    HORIZONTAL_SPACE = 10
    BUTTON_HEIGHT = 50
    USABLE_AREA_WIDTH = 240
    WIDE_BUTTON_SIZE = USABLE_AREA_WIDTH
    narrow_button_size = 115

    def __init__(self, header="", buttons={}):
        self._header = header
        self._buttons = []

        current_height = Page.HEADER_HEIGHT
        current_width = Page.MARGIN_LEFT
        for button_type, button in buttons:
            button_id, label = button
            if button_type == ButtonType.TEXT_NARROW:
                self._buttons.append(TextButton(pos_x=current_width,
                                                pos_y=current_height,
                                                width=Page.USABLE_AREA_WIDTH / 2 - 5,
                                                height=Page.BUTTON_HEIGHT,
                                                text=label,
                                                id=button_id))
                current_width += self._buttons[-1].get_width() + Page.HORIZONTAL_SPACE
            elif button_type == ButtonType.TEXT_WIDE:
                self._buttons.append(TextButton(pos_x=Page.MARGIN_LEFT,
                                                pos_y=current_height,
                                                width=Page.USABLE_AREA_WIDTH,
                                                height=Page.BUTTON_HEIGHT,
                                                text=label,
                                                id=button_id))
                current_height += self._buttons[-1].get_height() + Page.VERTICAL_SPACE
            elif button_type == ButtonType.TEXT_AREA:
                self._buttons.append(TextButton(pos_x=Page.MARGIN_LEFT,
                                                pos_y=current_height,
                                                width=Page.USABLE_AREA_WIDTH,
                                                height=(Page.BUTTON_HEIGHT * 4 + Page.VERTICAL_SPACE * 3),
                                                text=label,
                                                id=button_id,
                                                is_disabled=True))
                current_height += self._buttons[-1].get_height() + Page.VERTICAL_SPACE
            elif button_type == ButtonType.MULTI_CHOICE_SHORT:
                self._buttons.append(MultiChoiceButton(pos_x=Page.MARGIN_LEFT,
                                                       pos_y=current_height,
                                                       width=Page.USABLE_AREA_WIDTH,
                                                       height=Page.BUTTON_HEIGHT,
                                                       choices=label,
                                                       id=button_id))
                current_height += self._buttons[-1].get_height() + Page.VERTICAL_SPACE
            elif button_type == ButtonType.MULTI_CHOICE_LONG:
                self._buttons.append(MultiChoiceButton(pos_x=Page.MARGIN_LEFT,
                                                       pos_y=current_height,
                                                       width=Page.USABLE_AREA_WIDTH,
                                                       height=Page.BUTTON_HEIGHT * 3 + Page.VERTICAL_SPACE * 2,
                                                       choices=label,
                                                       id=button_id))
                current_height += self._buttons[-1].get_height() + Page.VERTICAL_SPACE

        for i, button in enumerate(self._buttons):
            if not button.is_disabled():
                self._active_button_idx = self._default_active_button_idx = i
                break

    def move_up(self):
        if self._active_button_idx > 0:
            next_idx = self._active_button_idx - 1
            while self._buttons[next_idx].is_disabled():
                next_idx -= 1
                if next_idx < 0:
                    return
            self._active_button_idx = next_idx
            while self._active_button_idx > 0 and self._buttons[self._active_button_idx].get_width() == 115:
                self._active_button_idx -= 1

    def move_down(self):
        if self._active_button_idx < len(self._buttons) - 1:
            next_idx = self._active_button_idx + 1
            while self._buttons[next_idx].is_disabled():
                next_idx += 1
                if next_idx > len(self._buttons) - 1:
                    return
            self._active_button_idx = next_idx

    def move_left(self):
        if type(self._buttons[self._active_button_idx]) is MultiChoiceButton:
            self._buttons[self._active_button_idx].go_left()
        else:
            prev_idx = self._active_button_idx - 1
            if prev_idx >= 0 and self._buttons[prev_idx].get_width() == Page.narrow_button_size:
                self._active_button_idx -= 1

    def move_right(self):
        if type(self._buttons[self._active_button_idx]) is MultiChoiceButton:
            self._buttons[self._active_button_idx].go_right()
        else:
            next_idx = self._active_button_idx + 1
            if next_idx < len(self._buttons) and self._buttons[next_idx].get_width() == Page.narrow_button_size:
                self._active_button_idx += 1

    def get_active_choices(self):
        choices = []
        for button in self._buttons:
            if type(button) is MultiChoiceButton:
                choices.append(button.get_id())
        return choices

    def get_current_button_id(self):
        return self._buttons[self._active_button_idx].get_id()

    def reset_current_button(self):
        self._active_button_idx = self._default_active_button_idx

    def render(self, window):
        window.fill(LayoutRsc.WINDOW_COLOR)
        Text.render_centered_text(surface=window,
                                  center_x=LayoutRsc.WINDOW_WIDTH / 2,
                                  center_y=Page.HEADER_HEIGHT / 2,
                                  font=FontRsc.HEADER_FONT,
                                  text=self._header,
                                  color=FontRsc.HEADER_FONT_COLOR)

        for i, button in enumerate(self._buttons):
            if i == self._active_button_idx:
                button.draw_highlighted(window)
            else:
                button.draw_regular(window)
