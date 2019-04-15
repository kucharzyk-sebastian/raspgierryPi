import pygame.font

if not pygame.font.get_init():
    pygame.font.init()


class FontRsc:
    CONTENT_FONT_SMALL = pygame.font.Font("SFPixelate.ttf", 17)
    CONTENT_FONT_REGULAR = pygame.font.Font("SFPixelate.ttf", 24)
    CONTENT_FONT_COLOR = (203, 200, 60)

    MONOSPACE_FONT = pygame.font.Font("basis33.ttf", 40)

    HEADER_FONT = pygame.font.Font("VT323.ttf", 48)
    HEADER_FONT_COLOR = (34, 186, 51)
