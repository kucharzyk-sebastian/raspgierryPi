import pygame.draw
from src.gui.button import *
from src.resources.font_rsc import *
from src.resources.layout_rsc import *
from src.helpers.text import *


class MultiChoiceButton(Button):

    def __init__(self, pos_x, pos_y, width, height, choices, id):
        Button.__init__(self, pos_x, pos_y, width, height, id)
        self._current_choice = 0
        self._choices = []
        for choice_id, choice_label in choices.items():
            try:
                img = pygame.image.load(LayoutRsc.TEXTURES_PATH + 'buttons\\' + choice_label + '.png')
                self._choices.append((choice_id, img))
            except pygame.error:
                self._choices.append((choice_id, choice_label))

    def get_id(self):
        return self._choices[self._current_choice][0]

    def go_left(self):
        if self._current_choice > 0:
            self._current_choice -= 1
        else:
            self._current_choice = len(self._choices) - 1

    def go_right(self):
        if self._current_choice < len(self._choices) - 1:
            self._current_choice += 1
        else:
            self._current_choice = 0

    def draw_images_if_needed(self, window):
        choice_id, choice_content = self._choices[self._current_choice]
        if type(choice_content) is pygame.Surface:
            window.blit(choice_content, (self._x, self._y))
        else:
            Text.render_centered_text(window, self._x + self._width / 2, self._y + self._height / 2 + self._height * 0.08, FontRsc.CONTENT_FONT_REGULAR, choice_content, FontRsc.CONTENT_FONT_COLOR)

    def draw_arrows(self, window):
        pygame.draw.line(window, LayoutRsc.LINE_COLOR, (self._x + 5, self._y + self._height / 2), (self._x + 20, self._y + self._height / 2 - 15), LayoutRsc.LINE_THICKNESS)
        pygame.draw.line(window, LayoutRsc.LINE_COLOR, (self._x + 5, self._y + self._height / 2), (self._x + 20, self._y + self._height / 2 + 15), LayoutRsc.LINE_THICKNESS)

        pygame.draw.line(window, LayoutRsc.LINE_COLOR, (self._x + self._width - 5, self._y + self._height / 2), (self._x + self._width - 20, self._y + self._height / 2 - 15), LayoutRsc.LINE_THICKNESS)
        pygame.draw.line(window, LayoutRsc.LINE_COLOR, (self._x + self._width - 5, self._y + self._height / 2), (self._x + self._width - 20, self._y + self._height / 2 + 15), LayoutRsc.LINE_THICKNESS)

    def draw_regular(self, window):
        super().draw_regular(window)
        self.draw_images_if_needed(window)
        self.draw_arrows(window)

    def draw_highlighted(self, window):
        super().draw_highlighted(window)
        self.draw_images_if_needed(window)
        self.draw_arrows(window)
