from src.resources.layout_rsc import *
from src.resources.sound_rsc import *
from src.games.game import *
from src.controls.joystick import *
import pygame
from src.settings import GameLevel

class SnakePart(pygame.sprite.Sprite):
    PART_SIZE = (10, 10)
    TEXTURE_PATH = LayoutRsc.TEXTURES_PATH + '/snake/snake.png'

    def __init__(self,
                 belongs_to,
                 rect = pygame.Rect(LayoutRsc.GAME_AREA_HEIGHT / 2, LayoutRsc.GAME_AREA_HEIGHT / 2, *PART_SIZE)
                 ):
        pygame.sprite.Sprite.__init__(self, belongs_to)
        self.image = pygame.transform.scale(pygame.image.load(SnakePart.TEXTURE_PATH), SnakePart.PART_SIZE)
        self.rect = self.image.get_rect()
        self.rect = rect
        self._alive_cycles = 0
        self._group = belongs_to

    def update(self):
        self._alive_cycles += 1
        if self._alive_cycles == len(self._group):
            self.kill();


class Snake():
    def __init__(self, starting_pos_x, starting_pos_y, speed):
        self._direction = "up"
        self._isAlive = True
        self._pointsOccupied = pygame.sprite.Group()
        self._head = SnakePart(self._pointsOccupied)
        self._snake_speed = speed
        self._time_since_last_update = self._snake_speed

    def set_direction(self, direction):
        allowed_directions = ["up", "down", "right", "left"]
        if direction not in allowed_directions:
            raise Exception("not allowed direction")
        self._direction = direction

    def get_occupied_points(self):
        return self._pointsOccupied

    def calculate_new_head_rect(self, old_head):
        shift_val = old_head.rect.width  # it's square so no difference if width or height
        if self._direction == "left":
            return old_head.rect.move(-shift_val, 0)
        elif self._direction == "right":
            return old_head.rect.move(shift_val, 0)
        elif self._direction == "up":
            return old_head.rect.move(0, -shift_val)
        elif self._direction == "down":
            return old_head.rect.move(0, shift_val)

    def move(self):
        new_head_rect = self.calculate_new_head_rect(self._head)
        self._head = SnakePart(self._pointsOccupied, new_head_rect)

    def get_snake_size(self):
        return len(self._pointsOccupied)

    def draw(self, window):
        self._pointsOccupied.draw(window)

    def update(self, delta_time):
        self._time_since_last_update -= delta_time
        if (self._time_since_last_update <= 0):
            self._pointsOccupied.update()
            self.move()
            self._time_since_last_update = self._snake_speed

class SnakeGame(Game):

    SPEEDS = {GameLevel.Easy: 0.5, GameLevel.Medium: 0.3, GameLevel.Hard: 0.1}
    def __init__(self, level, is_sound_on):
        Game.__init__(self, level, is_sound_on)
        self._snake = Snake(LayoutRsc.GAME_AREA_WIDTH / 2, LayoutRsc.GAME_AREA_HEIGHT / 2, SnakeGame.SPEEDS[self._level])
        self.update_counter = 0

    def process_events(self, joystick):
        for event in pygame.event.get():
            joystick.process_event(event)

            if event.type in {JOYBUTTONUP, JOYBUTTONDOWN, JOYAXISMOTION}:
                if joystick.is_arrow_updir_pressed():
                    self._snake.set_direction("up")
                if joystick.is_arrow_downdir_pressed():
                    self._snake.set_direction("down")
                if joystick.is_arrow_leftdir_pressed():
                    self._snake.set_direction("left")
                if joystick.is_arrow_rightdir_pressed():
                    self._snake.set_direction("right")

    def update(self, delta_time):
        self._snake.update(delta_time)

    def render(self, window):
        window.fill(LayoutRsc.WINDOW_COLOR)
        self._snake.draw(window)

    def is_running(self):
        return self._is_running

    def get_points(self):  # TODO jagros: it's confusing, should be scoree
        return self._points

    def get_lives(self):
        return self._lives
