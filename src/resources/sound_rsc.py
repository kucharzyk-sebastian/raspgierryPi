import pygame.mixer

if not pygame.mixer.get_init():
    pygame.mixer.init()


class SoundRsc:
    sounds_path = '../resources/sounds/'
    button_click = pygame.mixer.Sound(sounds_path + 'menu/button_click.wav')
    button_switch = pygame.mixer.Sound(sounds_path + 'menu/button_switch.wav')
