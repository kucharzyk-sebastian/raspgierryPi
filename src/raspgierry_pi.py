import pygame, sys
from pygame.locals import *
from controls.joystick import *

class RaspgierryPi:
    def __init__(self):
        pygame.init()
        self._display = {'width': 320, 'height': 480}
        native_screen = pygame.display.Info()
        if native_screen.current_w < self._display['width'] or native_screen.current_h < self._display['height']:
            # TODO sk: Add error screen for minimum display when available
            sys.exit(1)
        self._display_ratio = native_screen.current_w /  self._display['width']
        self._window = pygame.display.set_mode((0,0), FULLSCREEN)
        pygame.display.set_caption('Raspgierry Pi')
        
    def run(self):
        while True:
            self._process_events()
            self._update()
            self._render()
    
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
