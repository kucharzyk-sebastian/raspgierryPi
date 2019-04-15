from src.games.game import *
import pygame.display

class Galaxian(Game):
    def __init__(self, level, sound_on):
        Game.__init__(self, level, sound_on)

    def render(self, window):
        pygame.display.update()
