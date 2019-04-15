from src.resources.layout_rsc import *
from src.resources.font_rsc import *
from src.gui.indented_rect import *
from src.helpers.text import *


class Hud:
    top_margin = 20
    side_margin = 20
    top_bar_height = 50
    game_area_height = 370
    top_bar_inner_margin = 10
    heart_spacing = 5
    heart_texture_size = (29, 25)
    heart_texture_path = LayoutRsc.TEXTURES_PATH + 'hud\\heart.png'
    area_width = LayoutRsc.WINDOW_WIDTH - side_margin * 2

    def __init__(self):
        self._lives = 3
        self._points = 0
        self._top_bar_rect = IndentedRect(Hud.side_margin, Hud.top_margin, Hud.area_width, Hud.top_bar_height)
        self._game_area_rect = IndentedRect(Hud.side_margin, Hud.top_margin + self._top_bar_rect.get_height() + Hud.top_margin, Hud.area_width, Hud.game_area_height)
        self._heart_texture = pygame.transform.scale(pygame.image.load(Hud.heart_texture_path), Hud.heart_texture_size)

    def draw(self, window):
        self._top_bar_rect.draw(window, LayoutRsc.ITEM_REGULAR_BG_COLOR)
        for i in range(0, self._lives):
            heart_rect = self._heart_texture.get_rect()
            heart_rect.center = (Hud.side_margin + Hud.top_bar_inner_margin + self._heart_texture.get_width() / 2 + (self._heart_texture.get_width() + Hud.heart_spacing) * i, Hud.top_margin + Hud.top_bar_height / 2)
            window.blit(self._heart_texture, heart_rect)
            points = "{0:0=5d}".format(self._points)
            text_width, text_height = FontRsc.MONOSPACE_FONT.size(points)
            Text.render_centered_text(window, LayoutRsc.WINDOW_WIDTH - Hud.side_margin - text_width / 2 - Hud.top_bar_inner_margin, Hud.top_margin + Hud.top_bar_height / 2 + 2, FontRsc.MONOSPACE_FONT, points, (200, 200, 200))

        self._game_area_rect.draw(window, LayoutRsc.ITEM_REGULAR_BG_COLOR)
