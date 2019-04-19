from src.games.game import *


class Snake(Game):
    def __init__(self, level, is_sound_on, game_type):
        Game.__init__(self, level, is_sound_on, game_type)
