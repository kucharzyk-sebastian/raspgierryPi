from src.resources.font_rsc import *
from src.helpers.text import *
from src.gui.indented_rect import *


class Hud:
    SIDE_MARGIN = (LayoutRsc.WINDOW_WIDTH - LayoutRsc.GAME_AREA_WIDTH) / 2
    TOP_MARGIN = 20

    BORDER_WIDTH = LayoutRsc.LINE_THICKNESS
    USABLE_AREA_WIDTH = LayoutRsc.GAME_AREA_WIDTH + BORDER_WIDTH * 2

    TOP_BAR_HEIGHT = 50
    TOP_BAR_INNER_MARGIN = 10
    HEART_SPACING = 5
    HEART_TEXTURE_SIZE = (29, 25)
    HEART_TEXTURE_PATH = LayoutRsc.TEXTURES_PATH + 'hud/heart.png'

    GAME_RECT_HEIGHT = LayoutRsc.GAME_AREA_HEIGHT + BORDER_WIDTH * 2

    def __init__(self, game):
        self._game = game
        self._lives = 3
        self._points = 0
        self._top_bar_rect = IndentedRect(pos_x=Hud.SIDE_MARGIN,
                                          pos_y=Hud.TOP_MARGIN,
                                          width=Hud.USABLE_AREA_WIDTH,
                                          height=Hud.TOP_BAR_HEIGHT)
        self._game_rect = IndentedRect(pos_x=Hud.SIDE_MARGIN,
                                       pos_y=Hud.TOP_MARGIN + self._top_bar_rect.get_height() + Hud.TOP_MARGIN,
                                       width=Hud.USABLE_AREA_WIDTH,
                                       height=Hud.GAME_RECT_HEIGHT)
        self._heart_texture = pygame.transform.scale(pygame.image.load(Hud.HEART_TEXTURE_PATH), Hud.HEART_TEXTURE_SIZE)
        self._game_surface = pygame.Surface((LayoutRsc.GAME_AREA_WIDTH, LayoutRsc.GAME_AREA_HEIGHT),
                                            pygame.SRCALPHA, 32)

    def is_running(self):
        return self._game.is_running()

    def process_events(self, joystick):
        self._game.process_events(joystick)

    def update(self, time_per_frame):
        self._game.update(time_per_frame)

    def render(self, window):
        self._render_top_bar(window)
        self._render_game_area(window)
        pygame.display.update()

    def _render_top_bar(self, window):
        window.fill(LayoutRsc.WINDOW_COLOR)
        self._top_bar_rect.draw(window, LayoutRsc.ITEM_REGULAR_BG_COLOR)
        for i in range(0, self._lives):
            heart_rect = self._heart_texture.get_rect()
            first_hear_center = Hud.SIDE_MARGIN + Hud.TOP_BAR_INNER_MARGIN + self._heart_texture.get_width() / 2
            heart_rect.center = (first_hear_center + (self._heart_texture.get_width() + Hud.HEART_SPACING) * i,
                                 Hud.TOP_MARGIN + Hud.TOP_BAR_HEIGHT / 2)
            window.blit(self._heart_texture, heart_rect)

        points = "{0:0=5d}".format(self._points)
        text_width, text_height = FontRsc.MONOSPACE_FONT.size(points)
        Text.render_centered_text(window, LayoutRsc.WINDOW_WIDTH - Hud.SIDE_MARGIN -
                                  text_width / 2 - Hud.TOP_BAR_INNER_MARGIN,
                                  Hud.TOP_MARGIN + Hud.TOP_BAR_HEIGHT / 2 + 2,
                                  FontRsc.MONOSPACE_FONT, points, FontRsc.MONOSPACE_FONT_COLOR)

    def _render_game_area(self, window):
        self._game_rect.draw(window, LayoutRsc.ITEM_REGULAR_BG_COLOR)
        self._game.render(self._game_surface)
        window.blit(self._game_surface,
                    (self._game_rect.get_pos_x() + Hud.BORDER_WIDTH, self._game_rect.get_pos_y() + Hud.BORDER_WIDTH))
