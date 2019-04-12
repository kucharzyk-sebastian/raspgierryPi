import pygame.font

if not pygame.font.get_init():
    pygame.font.init()


class FontRsc:
    paragraph_font = pygame.font.Font("SFPixelate.ttf", 17)
    content_font = pygame.font.Font("SFPixelate.ttf", 24)
    header_font = pygame.font.Font("VT323.ttf", 48)
    header_font_color = (34, 186, 51)
