from src.gui.text_button import *
from src.gui.multi_choice_button import *

class ButtonType(Enum):
    Play = 0
    Settings = 1
    Scores = 2
    Exit = 3
    About = 4
    Help = 5
    SoundOn = 6
    Controls = 7
    Easy = 8
    Medium = 9
    Hard = 10
    Back = 11
    Empty = 12

class Page:
    header_height = 100
    margin_left = 40
    vertical_space = 20
    horizontal_space = 10

    def __init__(self, header="", text_area_lines=[], wide_button_labels={}, narrow_button_labels={}, selectable_area_long=[], selectable_area_short=[]):
        self._header = header
        self._text_area_lines = text_area_lines
        self.wide_buttons_labels = wide_button_labels
        self.narrow_buttons_labels = narrow_button_labels
        self.selectable_area_short = selectable_area_short
        self.selectable_area_long = selectable_area_long
        self.text_area = None
        self._buttons = []

        current_height = Page.header_height
        # TODO sk: remove hardcoded ButtonType
        if self._text_area_lines:
            self._buttons.append(TextButton(Page.margin_left, current_height, TextButtonWidth.WIDE, (TextButtonHeight.REGULAR.value * 4 + Page.vertical_space * 3), self._text_area_lines, ButtonType.Hard, True))
            current_height += self._buttons[-1].get_height() + Page.vertical_space

        if self.selectable_area_long:
            self._buttons.append(
                MultiChoiceButton(Page.margin_left, current_height, self.selectable_area_long, MultiChoiceButtonSize.LONG, True))
            current_height += self._buttons[-1].get_height() + Page.vertical_space

        if self.selectable_area_short:
            self._buttons.append(
                MultiChoiceButton(Page.margin_left, current_height, self.selectable_area_short, MultiChoiceButtonSize.SHORT, False))
            current_height += self._buttons[-1].get_height() + Page.vertical_space

        for type, label in self.wide_buttons_labels.items():
            if label is not None:
                self._buttons.append(TextButton(Page.margin_left, current_height, TextButtonWidth.WIDE, TextButtonHeight.REGULAR.value, label, type))
                current_height += self._buttons[-1].get_height() + Page.vertical_space
            else:
                current_height += TextButton.height + Page.vertical_space

        current_width = Page.margin_left
        for type, label in self.narrow_buttons_labels.items():
            self._buttons.append(TextButton(current_width, current_height, TextButtonWidth.NARROW, TextButtonHeight.REGULAR.value, label, type))
            current_width += self._buttons[-1].get_width() + Page.horizontal_space

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
            while self._active_button_idx > 0 and self._buttons[self._active_button_idx].get_size() == TextButtonWidth.NARROW:
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
            if prev_idx >= 0 and self._buttons[prev_idx].get_size() == TextButtonWidth.NARROW:
                self._active_button_idx -= 1

    def move_right(self):
        if type(self._buttons[self._active_button_idx]) is MultiChoiceButton:
            self._buttons[self._active_button_idx].go_right()
        else:
            next_idx = self._active_button_idx + 1
            if next_idx < len(self._buttons) and self._buttons[next_idx].get_size() == TextButtonWidth.NARROW:
                self._active_button_idx += 1

    def get_chosen_button(self):
        return self._buttons[self._active_button_idx].get_type()

    def reset_chosen_button(self):
        self._active_button_idx = self._default_active_button_idx

    def render(self, window):
        window.fill(LayoutRsc.window_color)
        Text.render_centered_text(window, LayoutRsc.window_width / 2, Page.header_height / 2, FontRsc.header_font, self._header,
                                  FontRsc.header_font_color)

        if self.text_area:
            self.text_area.draw(window)

        for i, button in enumerate(self._buttons):
            if i == self._active_button_idx:
                button.draw_highlighted(window)
            else:
                button.draw_regular(window)
