import pygame.mixer

if not pygame.mixer.get_init():
    pygame.mixer.init()


class SoundRsc:
    sounds_path = '../resources/sounds/'
    button_click = pygame.mixer.Sound(sounds_path + 'menu/button_click.wav')
    button_switch = pygame.mixer.Sound(sounds_path + 'menu/button_switch.wav')

    enemy_death = pygame.mixer.Sound(sounds_path + 'galaxian/enemy_death.wav')
    projectile_launch = pygame.mixer.Sound(sounds_path + 'galaxian/projectile_launch.wav')
