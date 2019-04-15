import pygame.draw
from src.resources.font_rsc import *
from src.helpers.text import *
from src.gui.button import *


class MultiChoiceButton(Button):

    def __init__(self, pos_x, pos_y, width, height, choices, id):
        Button.__init__(self, pos_x, pos_y, width, height, id)
        self._current_choice = 0
        self._choices = []
        for choice_id, choice_label in choices.items():
            try:
                img = pygame.image.load(LayoutRsc.TEXTURES_PATH + 'buttons/' + choice_label + '.png')
            except pygame.error:
                self._choices.append((choice_id, choice_label))
            else:
                self._choices.append((choice_id, img))

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

    def draw_focused(self, window):
        super().draw_focused(window)
        self._draw_images_if_needed(window)
        self._draw_arrows(window)

    def draw_not_focused(self, window):
        super().draw_not_focused(window)
        self._draw_images_if_needed(window)
        self._draw_arrows(window)

    def _draw_images_if_needed(self, window):
        choice_id, choice_content = self._choices[self._current_choice]
        if type(choice_content) is pygame.Surface:
            window.blit(choice_content, (self._x, self._y))
        else:
            Text.render_centered_text(surface=window,
                                      center_x=self._x + self._width / 2,
                                      center_y=self._y + self._height / 2 + self._height * 0.08,
                                      font=FontRsc.CONTENT_FONT_REGULAR,
                                      text=choice_content,
                                      color=FontRsc.CONTENT_FONT_COLOR)

    def _draw_arrows(self, window):
        pygame.draw.line(window,
                         LayoutRsc.LINE_COLOR,
                         (self._x + 5, self._y + self._height / 2),
                         (self._x + 20, self._y + self._height / 2 - 15),
                         LayoutRsc.LINE_THICKNESS)

        pygame.draw.line(window,
                         LayoutRsc.LINE_COLOR,
                         (self._x + 5, self._y + self._height / 2),
                         (self._x + 20, self._y + self._height / 2 + 15),
                         LayoutRsc.LINE_THICKNESS)

        pygame.draw.line(window,
                         LayoutRsc.LINE_COLOR,
                         (self._x + self._width - 5,
                          self._y + self._height / 2),
                         (self._x + self._width - 20, self._y + self._height / 2 - 15),
                         LayoutRsc.LINE_THICKNESS)

        pygame.draw.line(window,
                         LayoutRsc.LINE_COLOR,
                         (self._x + self._width - 5, self._y + self._height / 2),
                         (self._x + self._width - 20, self._y + self._height / 2 + 15),
                         LayoutRsc.LINE_THICKNESS)
