import pygame
from pygame.locals import *
from src.helpers.dotdict import *

class Joystick:
    def __init__(self, joystick_id):
        if not pygame.joystick.get_init():
            pygame.joystick.init()
        self._joystick = pygame.joystick.Joystick(joystick_id)
        self._joystick.init()
        self._is_button_pressed = dotdict({
            "a": False,
            "b": False,
            "x": False,
            "y": False,
        })
        self._is_joy_pressed = dotdict({
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

    def is_joy_up_pressed(self):
        return self._is_joy_pressed.up

    def is_joy_down_pressed(self):
        return self._is_joy_pressed.down

    def is_joy_left_pressed(self):
        return self._is_joy_pressed.left

    def is_joy_right_pressed(self):
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
    def _process_axis_direction(axis_dict, axis_value, lower_bound, upper_bound):
        if axis_value <= -1:
            axis_dict[lower_bound] = True
        elif axis_value >= 1:
            axis_dict[upper_bound] = True
        else:
            axis_dict[lower_bound] = False
            axis_dict[upper_bound] = False
