import pygame

from src.games.game import *
from src.games.racing.board import Board
from src.games.racing.enemy import Enemy
from src.games.racing.player import Player
from src.resources.layout_rsc import LayoutRsc
from pygame import *

from random import randrange

from src.settings import GameLevel


class Racing(Game):
    GAME_SPEEDS = {  # TODO jagros: find better name
        GameLevel.Easy : 0.5,
        GameLevel.Medium : 0.2,
        GameLevel.Hard : 0.1,
    }
    def __init__(self, level, is_sound_on):
        Game.__init__(self, level, is_sound_on)
        self._board = Board(LayoutRsc.GAME_AREA_WIDTH, LayoutRsc.GAME_AREA_HEIGHT, 2, 20)
        self._roadway_width = LayoutRsc.GAME_AREA_WIDTH/2
        self._player = Player(self._board, self._roadway_width)
        self._group_of_enemies = sprite.Group()
        self._game_speed = Racing.GAME_SPEEDS[level]
        self._time_since_last_update = self._game_speed

    def process_events(self, joystick):
        for event in pygame.event.get():
            joystick.process_event(event)
            if event.type in {JOYBUTTONUP, JOYBUTTONDOWN, JOYAXISMOTION}:
                if joystick.is_arrow_leftdir_pressed():
                    self._player.take_roadway("left")
                if joystick.is_arrow_rightdir_pressed():
                    self._player.take_roadway("right")

    def update(self, delta_time):
        self._time_since_last_update -= delta_time
        if self._time_since_last_update <= 0:
            self._player.update()
            self._group_of_enemies.update()
            self._create_enemy_if_possible()
            self._time_since_last_update = self._game_speed

    def render(self, window):
        window.fill(LayoutRsc.WINDOW_COLOR)
        self._player.render(window)
        self._group_of_enemies.draw(window)

    def is_running(self):
        return self._has_player_collided()

    def _has_player_collided(self):
        list_of_enemies_rect = [x.rect for x in self._group_of_enemies.sprites()]
        return self._player.rect.collidelist(list_of_enemies_rect)

    def get_points(self):
        return self._points

    def get_lives(self):
        return self._lives

    def _create_enemy_if_possible(self):  # TODO jagros: write a better algorithm
        if len(self._group_of_enemies) == 0:
            roadway_to_take = randrange(1)
            new_enemy = Enemy(self._group_of_enemies, self._board, self._roadway_width, roadway_to_take)


