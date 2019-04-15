import pygame.font

if not pygame.font.get_init():
    pygame.font.init()


class FontRsc:
    FONTS_PATH = "..\\resources\\fonts\\"
    CONTENT_FONT_SMALL = pygame.font.Font(FONTS_PATH + "SFPixelate.ttf", 17)
    CONTENT_FONT_REGULAR = pygame.font.Font(FONTS_PATH + "SFPixelate.ttf", 24)
    CONTENT_FONT_COLOR = (203, 200, 60)

    MONOSPACE_FONT = pygame.font.Font(FONTS_PATH + "basis33.ttf", 40)
    MONOSPACE_FONT_COLOR = (200, 200, 200)

    HEADER_FONT = pygame.font.Font(FONTS_PATH + "VT323.ttf", 48)
    HEADER_FONT_COLOR = (34, 186, 51)
