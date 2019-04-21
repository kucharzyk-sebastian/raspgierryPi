from random import randrange

import pygame
from pygame import *

from src.games.game import *
from src.games.racing.board import Board
from src.games.racing.enemy import Enemy
from src.games.racing.player import Player
from src.games.racing.settings import Settings
from src.resources.layout_rsc import LayoutRsc


class Racing(Game):

    def __init__(self, level, is_sound_on):
        Game.__init__(self, level, is_sound_on)
        self._board = Board(LayoutRsc.GAME_AREA_WIDTH, LayoutRsc.GAME_AREA_HEIGHT, *Settings.BOARD_FIELDS)
        self._player = Player(self._board)
        self._group_of_enemies = sprite.Group()
        self._game_speed = Settings.GAME_SPEEDS[level]
        self._time_since_last_update = self._game_speed
        self._level = level
        self._points_as_float = 0.0
        self._empty_buffer_rect = Rect((0, -Settings.CAR_SIZE[1]),
                                       (LayoutRsc.GAME_AREA_WIDTH, 2 * Settings.CAR_SIZE[1]))
        self._points_earned_per_update = 1 / 2 * Settings.GAME_SPEEDS_SCORE_BONUS[self._level]

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
            self._create_enemy_if_possible()
            self._group_of_enemies.update()
            self._time_since_last_update = self._game_speed
            self._points_as_float += self._points_earned_per_update
            self._points = int(self._points_as_float)

    def render(self, window):
        window.fill(LayoutRsc.WINDOW_COLOR)
        self._draw_road_lines(window)
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

    def _create_enemy_if_possible(self):
        enemy_rect_list = [x.rect for x in self._group_of_enemies.sprites()]
        if len(enemy_rect_list) == 0 or self._empty_buffer_rect.collidelist(enemy_rect_list) == -1:
            if randrange(100) < 30:  # 30% likelihood of generating car
                roadway_to_take = randrange(2)
                Enemy(self._group_of_enemies, self._board, roadway_to_take)

    def _draw_road_lines(self, window):
        draw.line(window,
                  Settings.WHITE,
                    (Settings.OUTER_ROADLINE_MARGIN_X, Settings.OUTER_ROADLINE_MARGIN_Y),
                  (Settings.OUTER_ROADLINE_MARGIN_X, LayoutRsc.GAME_AREA_HEIGHT - Settings.OUTER_ROADLINE_MARGIN_Y),
                  Settings.ROADLINE_LINE_WIDTH)

        draw.line(window,
                  Settings.WHITE,
                  (LayoutRsc.GAME_AREA_WIDTH - Settings.OUTER_ROADLINE_MARGIN_X, Settings.OUTER_ROADLINE_MARGIN_Y),
                  (LayoutRsc.GAME_AREA_WIDTH - Settings.OUTER_ROADLINE_MARGIN_X, LayoutRsc.GAME_AREA_HEIGHT - Settings.OUTER_ROADLINE_MARGIN_Y),
                  Settings.ROADLINE_LINE_WIDTH)

        middle = LayoutRsc.GAME_AREA_WIDTH / 2
        for y in range(LayoutRsc.GAME_AREA_HEIGHT):
            if int(y / Settings.ROADLINE_LINE_WIDTH) % 2 == 0:
                draw.line(window, Settings.WHITE, (middle, y), (middle, y), Settings.ROADLINE_LINE_WIDTH)
