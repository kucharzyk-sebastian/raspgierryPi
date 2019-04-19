from src.resources.layout_rsc import *
from src.resources.sound_rsc import *


class GalaxianRsc:
    ENEMY_TEXTURE_PATH = LayoutRsc.TEXTURES_PATH + '/galaxian/enemy.png'
    SPECIAL_ENEMY_TEXTURE_PATH = LayoutRsc.TEXTURES_PATH + '/galaxian/special_enemy.png'
    PROJECTILE_TEXTURE_PATH = LayoutRsc.TEXTURES_PATH + '/galaxian/projectile.png'
    PLAYER_TEXTURE_PATH = LayoutRsc.TEXTURES_PATH + '/galaxian/ship.png'

    ENEMY_DEATH = pygame.mixer.Sound(SoundRsc.sounds_path + 'galaxian/enemy_death.wav')
    PLAYER_DEATH = pygame.mixer.Sound(SoundRsc.sounds_path + 'galaxian/player_death.wav')
    SPECIAL_ENEMY_DEATH = pygame.mixer.Sound(SoundRsc.sounds_path + 'galaxian/special_enemy_death.wav')
    PROJECTILE_LAUNCH = pygame.mixer.Sound(SoundRsc.sounds_path + 'galaxian/projectile_launch.wav')
    ENEMY_GETS_CLOSER = pygame.mixer.Sound(SoundRsc.sounds_path + 'galaxian/enemy_gets_closer.wav')
    GAME_OVER = pygame.mixer.Sound(SoundRsc.sounds_path + 'menu/game_over.wav')
