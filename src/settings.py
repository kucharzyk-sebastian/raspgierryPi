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
    def __init__(self, sound_on=True, game=GameType.Galaxian, game_level=GameLevel.Easy):
        self.SoundOn = sound_on
        self.GameType = game
        self.GameLevel = game_level
