from src.settings import GameLevel
from src.resources.layout_rsc import LayoutRsc


class Settings:
    GAME_SPEEDS = {  # TODO jagros: find better name
        GameLevel.Easy: 0.5,
        GameLevel.Medium: 0.2,
        GameLevel.Hard: 0.1,
    }

    GAME_SPEEDS_SCORE_BONUS = {
        GameLevel.Easy: 1,
        GameLevel.Medium: 2,
        GameLevel.Hard: 3,
    }

    CAR_SIZE = (int(LayoutRsc.GAME_AREA_WIDTH * 0.15), int(LayoutRsc.GAME_AREA_HEIGHT * 0.2))
    BOARD_FIELDS = (2, 20)

    WHITE = (255, 255, 255)
    OUTER_ROADLINE_MARGIN_X = int(LayoutRsc.GAME_AREA_WIDTH * 0.05)  # TODO find better name
    OUTER_ROADLINE_MARGIN_Y = int(LayoutRsc.GAME_AREA_HEIGHT * 0.02)  # TODO find better name
    ROADLINE_LINE_WIDTH = int(LayoutRsc.GAME_AREA_WIDTH * 0.03) # TODO find better name
