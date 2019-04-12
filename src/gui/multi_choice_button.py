import pygame.draw
from enum import Enum
from src.gui.button import  *
from src.resources.font_rsc import *
from src.resources.layout_rsc import *
from src.helpers.text import *


class MultiChoiceButtonSize(Enum):
    LONG = 0
    SHORT = 1


class MultiChoiceButton(Button):

    def __init__(self, pos_x, pos_y, choices, size: MultiChoiceButtonSize, load_textures, type=None):
        if size == MultiChoiceButtonSize.SHORT:
            height = 50
        else:
            height = 190
        Button.__init__(self, pos_x, pos_y, LayoutRsc.usable_area_width, height, type)
        self._size = size
        self._choices = choices
        self._current_choice = 0
        self._images = []
        if load_textures:
            for choice in self._choices:
                self._images.append(pygame.image.load('D:\\dev\\raspgierryPi\\src\\img\\' + choice + '.png'))

    def get_size(self):
        return self._size

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
        if len(self._images) > 0:
            window.blit(self._images[self._current_choice], (self._x, self._y))
        else:
            Text.render_centered_text(window, self._x + self._width / 2, self._y + self._height / 2 + self._height * 0.08, FontRsc.content_font, self._choices[self._current_choice], LayoutRsc.line_color)

    def draw_arrows(self, window):
        pygame.draw.line(window, LayoutRsc.line_color, (self._x + 5, self._y + self._height/2), (self._x + 20, self._y + self._height/2 - 15),  LayoutRsc.line_thickness)
        pygame.draw.line(window, LayoutRsc.line_color, (self._x + 5, self._y + self._height/2), (self._x + 20, self._y + self._height/2 + 15),  LayoutRsc.line_thickness)

        pygame.draw.line(window, LayoutRsc.line_color, (self._x + self._width - 5, self._y + self._height/2), (self._x + self._width - 20, self._y + self._height/2 - 15),  LayoutRsc.line_thickness)
        pygame.draw.line(window, LayoutRsc.line_color, (self._x + self._width - 5, self._y + self._height/2), (self._x + self._width - 20, self._y + self._height/2 + 15),  LayoutRsc.line_thickness)

    def draw(self, window, bg_color):
        self.draw_shape(window, bg_color)
        self.draw_images_if_needed(window)
        self.draw_arrows(window)

