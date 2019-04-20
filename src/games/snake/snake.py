import pygame
from pygame import sprite
from src.games.snake.snake_part import SnakePart
from src.resources.snake_game_resources import SnakeGameResources
from src.resources.sound_rsc import SoundRsc
from src.settings import SnakeSettings


class Snake():
    def __init__(self, speed, board, is_sound_on):
        self._direction = SnakeSettings.SNAKE_INITIAL_DIRECTION
        self._prev_direction = self._direction
        self._isAlive = True
        self._pointsOccupied = sprite.Group()
        self._head = SnakeSettings.SNAKE_INITIAL_POSITION
        self._snake_speed = speed
        self._time_since_last_update = self._snake_speed
        self._board = board
        self._is_sound_on = is_sound_on
        self._create_body_part() # makes head of snake


    def _create_body_part(self, center_of_rect = None):
        if center_of_rect:
            SnakePart(self._pointsOccupied, self._board, center_of_rect)
        else:
            SnakePart(self._pointsOccupied, self._board)

    def get_head_rect(self):
        return self._board.get_rect(self._head['x'], self._head['y'])


    def set_direction(self, direction):
        allowed_directions = ["up", "down", "right", "left"]
        if direction not in allowed_directions:
            raise Exception("not allowed direction")

        # move in opposite direction only allowed if snake size is 1
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
        self._play_sound_if_needed(SnakeGameResources.EAT_FRUIT_SOUND_PATH)


    def move(self):
        new_head_rect = self.calculate_new_head_rect()
        self._create_body_part(new_head_rect.center)

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

    def get_opposite_direction(self, direction):
        opposite_directions = {
            "up": "down",
            "down": "up",
            "right": "left",
            "left": "right",
        }
        return opposite_directions[direction]


    def has_collided_with_itself(self):
        body_rect_list = [x.rect for x in self.get_occupied_points().sprites()]
        head_rect = self.get_head_rect()
        body_rect_list.remove(head_rect)
        has_collided = head_rect.collidelist(body_rect_list) >= 0
        if has_collided:
            self._play_sound_if_needed(SnakeGameResources.PLAYER_DEATH_SOUND_PATH)
        return has_collided


    def _play_sound_if_needed(self, sound):
        if self._is_sound_on:
            sound.play()
