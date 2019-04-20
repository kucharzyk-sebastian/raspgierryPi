from pygame import sprite
import pygame

from src.resources.layout_rsc import LayoutRsc
from src.resources.sound_rsc import SoundRsc


class SnakePart(pygame.sprite.Sprite):

    TEXTURE_PATH = LayoutRsc.TEXTURES_PATH + '/snake/snake.png'

    def __init__(self,
                 belongs_to,
                 board,
                 pos_center = None
                 ):
        pygame.sprite.Sprite.__init__(self, belongs_to)
        self._part_size = board.get_field_size()
        self.image = pygame.transform.scale(pygame.image.load(SnakePart.TEXTURE_PATH), self._part_size)
        self.rect = self.image.get_rect()
        if pos_center:
            self.rect.center = pos_center
        else:
            self.rect.center = board.get_middle().center
        self._group = belongs_to
        self._alive_cycles_left = len(self._group)

    def update(self):
        self._alive_cycles_left -=1
        if self._alive_cycles_left <= 0:
            self.kill()

    def increase_lifetime(self):
        self._alive_cycles_left += 1

class Snake():

    EAT_FRUIT = pygame.mixer.Sound(SoundRsc.sounds_path + 'snake/eat_fruit.wav')
    PLAYER_DEATH = pygame.mixer.Sound(SoundRsc.sounds_path + 'snake/player_death.wav')

    def __init__(self, speed, board, is_sound_on):
        self._direction = "up"
        self._prev_direction = self._direction
        self._isAlive = True
        self._pointsOccupied = sprite.Group()
        self._head = {"x": 0, "y": 0}
        self._snake_speed = speed
        self._time_since_last_update = self._snake_speed
        self._board = board
        SnakePart(self._pointsOccupied, self._board) #makes head
        self._is_sound_on = is_sound_on


    def get_head_rect(self):
        return self._board.get_rect(self._head['x'], self._head['y'])

    def set_direction(self, direction):
        allowed_directions = ["up", "down", "right", "left"]
        if direction not in allowed_directions:
            raise Exception("not allowed direction")

        # if length greater than 1 snake can't make moves in opposite way
        if len(self._pointsOccupied) == 1 or self.get_opposite_direction(self._direction) != direction:
            self._prev_direction = self._direction
            self._direction = direction


    def get_occupied_points(self):
        return self._pointsOccupied

    def calculate_new_head_rect(self):
        if self._direction == "left":
            self._head['x'] -= 1
        elif self._direction == "right":
            self._head['x'] += 1
        elif self._direction == "up":
            self._head['y'] -= 1
        elif self._direction == "down":
            self._head['y'] += 1
        return self._board.get_rect(self._head['x'], self._head['y'])

    def eat_fruit(self):
        self._board.remove_old_fruit_and_put_new(self)
        self._grow()
        self.play_sound_if_needed(Snake.EAT_FRUIT)

    def move(self):
        new_head_rect = self.calculate_new_head_rect()
        SnakePart(self._pointsOccupied, self._board, new_head_rect.center)

        if self._board.is_on_fruit_pos(new_head_rect):
            self.eat_fruit()

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

    def _grow(self):
        for part in self._pointsOccupied.sprites():
            part.increase_lifetime()

    def eat_fruit(self):
        self._board.remove_old_fruit_and_put_new(self)
        self._grow()
        self.play_sound_if_needed(Snake.EAT_FRUIT)

    def get_opposite_direction(self, direction):
        opposite_directions = {
            "up": "down",
            "down": "up",
            "right": "left",
            "left": "right",
        }
        return opposite_directions[direction]

    def has_collided_with_itself(self):
        sprites = self.get_occupied_points().sprites()
        body_rect_list = [x.rect for x in sprites]
        head_rect = self.get_head_rect()
        body_rect_list.remove(head_rect)
        has_collided = head_rect.collidelist(body_rect_list) >= 0
        if has_collided:
            self.play_sound_if_needed(Snake.PLAYER_DEATH)
        return has_collided

    def play_sound_if_needed(self, sound):
        if self._is_sound_on:
            sound.play()