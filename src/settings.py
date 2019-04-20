from enum import Enum


class GameType(Enum):
    Galaxian = 0
    Racing = 1
    Snake = 2


class GameLevel(Enum):
    Easy = 0
    Medium = 1
    Hard = 2

class SnakeSettings:
    SNAKE_SPEEDS = {
        GameLevel.Easy: 0.5,
        GameLevel.Medium: 0.3,
        GameLevel.Hard: 0.1
    }
    BOARD_FIELDS_HORIZONTALLY = 20
    BOARD_FIELDS_VERTICALLY = 20
    SNAKE_INITIAL_DIRECTION = "up"
    SNAKE_INITIAL_POSITION = {"x": 0, "y": 0}

class Settings:
    def __init__(self, is_sound_on=True, game=GameType.Galaxian, game_level=GameLevel.Easy):
        self.is_sound_on = is_sound_on
        self.game_type = game
        self.game_level = game_level
