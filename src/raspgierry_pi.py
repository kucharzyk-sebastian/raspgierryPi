import pygame
import sys
from pygame.locals import *
from controls.joystick import *
from gui.menu import *

class RaspgierryPi:

    def __init__(self):
        pygame.init()
        self._display = {'width': 320, 'height': 480}
        native_screen = pygame.display.Info()
        if native_screen.current_w < self._display['width'] or native_screen.current_h < self._display['height']:
            # TODO sk: Add error screen for minimum display when available
            sys.exit(1)
        self._window = pygame.display.set_mode((320, 480), RESIZABLE)
        pygame.display.set_caption('Raspgierry Pi')
        #TODO sk: check for ID and display error if not present
        self._joystick = Joystick(0)
        self._menu = Menu()
        
    def run(self):
        while True:
            self._process_intro_events()
            self._update_intro()
            self._render_intro()
        while True:
            self._process_events()
            self._update()
            self._render()

    def _process_intro_events(self):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                sys.exit(0)

            if event.type in {JOYBUTTONUP, JOYBUTTONDOWN, JOYAXISMOTION}:
                self._joystick.process_event(event)
                if self._joystick.is_a_pressed():
                    self._menu.get_into()
                if self._joystick.is_b_pressed():
                    print("B")
                if self._joystick.is_x_pressed():
                    print("X")
                if self._joystick.is_y_pressed():
                    print("Y")
                if self._joystick.is_arrow_downdir_pressed():
                    self._menu.move_down()
                if self._joystick.is_arrow_updir_pressed():
                    self._menu.move_up()
                if self._joystick.is_arrow_rightdir_pressed():
                    self._menu.move_right()
                if self._joystick.is_arrow_leftdir_pressed():
                    self._menu.move_left()


    def _update_intro(self):
        self._menu.update()

    def _render_intro(self):
        self._menu.render(self._window)
        pygame.display.update()

        
    def _process_events(self):
        for event in pygame.event.get():
            if event.type in {JOYBUTTONUP, JOYBUTTONDOWN, JOYAXISMOTION}:
                # TODO sk: Add joystick handling when available
                sys.exit(1)
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                sys.exit(0)
    
    def _update(self):
        #TODO sk: implement and remove printing
        print(0)
    
    def _render(self):
        pygame.display.update()
