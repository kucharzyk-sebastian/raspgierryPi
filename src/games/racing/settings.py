from src.resources.layout_rsc import LayoutRsc
from src.settings import GameLevel


class Settings:
    LVL_TO_REFRESH_TIME_MAP = {
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
    BUFFER_FIELDS_OUT_OF_BOARD = int(1 / 4 * BOARD_FIELDS[1])

    WHITE = (255, 255, 255)
    OUTER_ROAD_MARKING_MARGIN_X = int(LayoutRsc.GAME_AREA_WIDTH * 0.05)
    OUTER_ROAD_MARKING_MARGIN_Y = int(LayoutRsc.GAME_AREA_HEIGHT * 0.02)
    ROAD_LINE_LINE_WIDTH = int(LayoutRsc.GAME_AREA_WIDTH * 0.03)

    LIKELIHOOD_OF_GENERATING_ENEMY_PCT = 30

    AMOUNT_OF_LIVES = 3
