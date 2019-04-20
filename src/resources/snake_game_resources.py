from src.resources.layout_rsc import *
from src.resources.sound_rsc import *


class SnakeGameResources:
    SNAKE_PART_TEXTURE_PATH = LayoutRsc.TEXTURES_PATH + '/snake/snake.png'
    FRUIT_TEXTURE_PATH = LayoutRsc.TEXTURES_PATH + '/snake/fruit.png'
    EAT_FRUIT_SOUND_PATH = pygame.mixer.Sound(SoundRsc.sounds_path + 'snake/eat_fruit.wav')
    PLAYER_DEATH_SOUND_PATH = pygame.mixer.Sound(SoundRsc.sounds_path + 'snake/player_death.wav')
