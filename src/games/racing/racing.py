from random import randrange

import pygame
from pygame import *

from src.games.game import *
from src.games.racing.board import Board
from src.games.racing.enemy import Enemy
from src.games.racing.player import Player
from src.games.racing.settings import Settings as stngs
from src.resources.layout_rsc import LayoutRsc
from src.resources.racing_resources import RacingResources


class Racing(Game):
    CRASH_SOUND = pygame.mixer.Sound(RacingResources.CRASH_SOUND_PATH)

    def __init__(self, level, is_sound_on, game_type):
        Game.__init__(self, level, is_sound_on, game_type)
        self._board = Board(LayoutRsc.GAME_AREA_WIDTH, LayoutRsc.GAME_AREA_HEIGHT, * stngs.BOARD_FIELDS)
        self._player = Player(self._board)
        self._group_of_enemies = sprite.Group()
        self._refresh_time = stngs.LVL_TO_REFRESH_TIME_MAP[level]
        self._time_to_next_update = self._refresh_time
        self._level = level
        self._points_as_float = 0.0
        self._empty_buffer_rect = Rect((0, -stngs.CAR_SIZE[1]),
                                       (LayoutRsc.GAME_AREA_WIDTH, 2 * stngs.CAR_SIZE[1]))
        self._points_earned_per_update = stngs.POINTS_PER_UPDATE_FACTOR * stngs.GAME_SPEEDS_SCORE_BONUS[self._level]
        self._is_running = True
        self._lives = stngs.AMOUNT_OF_LIVES

    def process_events(self, joystick):
        for event in pygame.event.get():
            joystick.process_event(event)
            if event.type in {JOYBUTTONUP, JOYBUTTONDOWN, JOYAXISMOTION}:
                if joystick.is_arrow_leftdir_pressed():
                    self._player.take_roadway("left")
                if joystick.is_arrow_rightdir_pressed():
                    self._player.take_roadway("right")
                if joystick.is_y_pressed():
                    self._is_running = False

    def update(self, delta_time):
        self._time_to_next_update -= delta_time
        if self._time_to_next_update <= 0:
            self._player.update()
            self._create_enemy_if_possible()
            self._group_of_enemies.update()
            self._time_to_next_update = self._refresh_time
            self._points_as_float += self._points_earned_per_update
            self._points = int(self._points_as_float)

            if self._has_player_collided():
                self._die()

            if self._lives == 0:
                self._is_running = False

    def render(self, window):
        window.fill(LayoutRsc.WINDOW_COLOR)
        self._draw_road_lines(window)
        self._player.render(window)
        self._group_of_enemies.draw(window)

    def is_running(self):
        return self._is_running

    def _has_player_collided(self):
        list_of_enemies_rect = [x.rect for x in self._group_of_enemies.sprites()]
        if len(list_of_enemies_rect) == 0:
            return False
        return self._player.rect.collidelist(list_of_enemies_rect) != -1

    def get_points(self):
        return self._points

    def get_lives(self):
        return self._lives

    def _create_enemy_if_possible(self):
        enemy_rect_list = [x.rect for x in self._group_of_enemies.sprites()]
        if len(enemy_rect_list) == 0 or self._empty_buffer_rect.collidelist(enemy_rect_list) == -1:
            if randrange(100) < stngs.LIKELIHOOD_OF_GENERATING_ENEMY_PCT:
                roadway_to_take = randrange(2)
                Enemy(self._group_of_enemies, self._board, roadway_to_take)

    def _draw_road_lines(self, window):
        #left
        draw.line(window,
                  stngs.WHITE,
                  (stngs.OUTER_ROAD_MARKING_MARGIN_X, stngs.OUTER_ROAD_MARKING_MARGIN_Y),
                  (stngs.OUTER_ROAD_MARKING_MARGIN_X, LayoutRsc.GAME_AREA_HEIGHT - stngs.OUTER_ROAD_MARKING_MARGIN_Y),
                  stngs.ROAD_LINE_LINE_WIDTH)

        #right
        draw.line(window,
                  stngs.WHITE,
                  (LayoutRsc.GAME_AREA_WIDTH - stngs.OUTER_ROAD_MARKING_MARGIN_X, stngs.OUTER_ROAD_MARKING_MARGIN_Y),
                  (LayoutRsc.GAME_AREA_WIDTH - stngs.OUTER_ROAD_MARKING_MARGIN_X,
                   LayoutRsc.GAME_AREA_HEIGHT - stngs.OUTER_ROAD_MARKING_MARGIN_Y),
                  stngs.ROAD_LINE_LINE_WIDTH)

        #middle
        middle = LayoutRsc.GAME_AREA_WIDTH / 2
        for y in range(LayoutRsc.GAME_AREA_HEIGHT):
            if int(y / stngs.ROAD_LINE_LINE_WIDTH) % 2 == 0:
                draw.line(window, stngs.WHITE, (middle, y), (middle, y), stngs.ROAD_LINE_LINE_WIDTH)

    def _die(self):
        self._lives -= 1
        self._group_of_enemies.empty()
        self._play_sound_if_needed(Racing.CRASH_SOUND)

    def _play_sound_if_needed(self, sound):
        if self._is_sound_on:
            sound.play()
