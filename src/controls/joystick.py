import pygame
from src.helpers.dotdict import *
from pygame.locals import *


class Joystick:
    def __init__(self, joystick_id):
        if not pygame.joystick.get_init():
            pygame.joystick.init()
        self._joystick = pygame.joystick.Joystick(joystick_id)
        self._joystick.init()
        self._is_button_pressed = DotDict({
            "a": False,
            "b": False,
            "x": False,
            "y": False,
        })
        self._is_joy_pressed = DotDict({
            "up": False,
            "down": False,
            "left": False,
            "right": False
        })

    def process_event(self, event):
        if event.type == JOYBUTTONDOWN:
            self._process_button_event(event.button, True)
        elif event.type == JOYBUTTONUP:
            self._process_button_event(event.button, False)
        elif event.type == JOYAXISMOTION:
            self._process_axis_event(event.axis, event.value)

    def is_a_pressed(self):
        return self._is_button_pressed.a

    def is_b_pressed(self):
        return self._is_button_pressed.b

    def is_x_pressed(self):
        return self._is_button_pressed.x

    def is_y_pressed(self):
        return self._is_button_pressed.y

    def is_arrow_updir_pressed(self):
        return self._is_joy_pressed.up

    def is_arrow_downdir_pressed(self):
        return self._is_joy_pressed.down

    def is_arrow_leftdir_pressed(self):
        return self._is_joy_pressed.left

    def is_arrow_rightdir_pressed(self):
        return self._is_joy_pressed.right

    def _process_button_event(self, button_number, is_pressed):
        if button_number == 0:
            self._is_button_pressed.x = is_pressed
        elif button_number == 1:
            self._is_button_pressed.a = is_pressed
        elif button_number == 2:
            self._is_button_pressed.b = is_pressed
        elif button_number == 3:
            self._is_button_pressed.y = is_pressed

    def _process_axis_event(self, axis_id, axis_value):
        if axis_id == 1:
            self._process_axis_direction(self._is_joy_pressed, axis_value, "up", "down")
        elif axis_id == 0:
            self._process_axis_direction(self._is_joy_pressed, axis_value, "left", "right")

    @staticmethod
    def _process_axis_direction(axis_dict, axis_value, axis_positive, axis_negative):
        if axis_value <= -1:
            axis_dict[axis_positive] = True
        elif axis_value >= 1:
            axis_dict[axis_negative] = True
        else:
            axis_dict[axis_positive] = False
            axis_dict[axis_negative] = False
