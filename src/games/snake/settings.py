from src.settings import GameLevel


class SnakeSettings:
    SNAKE_SPEEDS = {
        GameLevel.Easy: 0.5,
        GameLevel.Medium: 0.3,
        GameLevel.Hard: 0.1
    }
    BOARD_FIELDS_HORIZONTALLY = 20
    BOARD_FIELDS_VERTICALLY = 20
    SNAKE_INITIAL_DIRECTION = "up"
    SNAKE_INITIAL_POSITION = {"x": 0, "y": BOARD_FIELDS_VERTICALLY - 1}
