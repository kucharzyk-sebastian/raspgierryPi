from enum import Enum


class GameType(Enum):
    Galaxian = 0
    Racing = 1
    Snake = 2


class GameLevel(Enum):
    Easy = 0
    Medium = 1
    Hard = 2

class Settings:
    def __init__(self, is_sound_on=True, game=GameType.Galaxian, game_level=GameLevel.Easy):
        self.is_sound_on = is_sound_on
        self.game_type = game
        self.game_level = game_level
