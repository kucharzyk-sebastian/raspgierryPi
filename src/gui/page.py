from src.gui.text_button import *
from src.gui.multi_choice_button import *
from enum import Enum


class ButtonType(Enum):
    TextNarrow = 0
    TextWide = 1
    MultiChoiceShort = 2
    MultiChoiceLong = 3
    TextArea = 4


class Page:
    header_height = 100
    margin_left = 40
    vertical_space = 20
    horizontal_space = 10
    button_height = 50
    wide_button_size = LayoutRsc.USABLE_AREA_WIDTH
    narrow_button_size = 115

    def __init__(self, header="", buttons={}):
        self._header = header
        self._buttons = []

        current_height = Page.header_height
        current_width = Page.margin_left
        for button_type, button in buttons:
            button_id, label = button
            if button_type == ButtonType.TextNarrow:
                self._buttons.append(TextButton(current_width, current_height, LayoutRsc.USABLE_AREA_WIDTH / 2 - 5, Page.button_height, label, button_id))
                current_width += self._buttons[-1].get_width() + Page.horizontal_space
            elif button_type == ButtonType.TextWide:
                self._buttons.append(TextButton(Page.margin_left, current_height, LayoutRsc.USABLE_AREA_WIDTH, Page.button_height, label, button_id))
                current_height += self._buttons[-1].get_height() + Page.vertical_space
            elif button_type == ButtonType.TextArea:
                self._buttons.append(TextButton(Page.margin_left, current_height, LayoutRsc.USABLE_AREA_WIDTH, (Page.button_height * 4 + Page.vertical_space * 3), label, button_id, True))
                current_height += self._buttons[-1].get_height() + Page.vertical_space
            elif button_type == ButtonType.MultiChoiceShort:
                self._buttons.append(MultiChoiceButton(Page.margin_left, current_height, LayoutRsc.USABLE_AREA_WIDTH, Page.button_height, label, button_id))
                current_height += self._buttons[-1].get_height() + Page.vertical_space
            elif button_type == ButtonType.MultiChoiceLong:
                self._buttons.append(MultiChoiceButton(Page.margin_left, current_height, LayoutRsc.USABLE_AREA_WIDTH, Page.button_height * 3 + Page.vertical_space * 2, label, button_id))
                current_height += self._buttons[-1].get_height() + Page.vertical_space

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
        Text.render_centered_text(window, LayoutRsc.WINDOW_WIDTH / 2, Page.header_height / 2, FontRsc.HEADER_FONT, self._header, FontRsc.HEADER_FONT_COLOR)

        for i, button in enumerate(self._buttons):
            if i == self._active_button_idx:
                button.draw_highlighted(window)
            else:
                button.draw_regular(window)
