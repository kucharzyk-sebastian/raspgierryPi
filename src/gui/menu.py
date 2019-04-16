import sys
from src.resources.sound_rsc import *
from src.gui.page import *
from src.settings import *
from src.controls.joystick import *
from src.games.galaxian.galaxian import *
from src.games.racing.racing import *
from src.games.snake.snake import *


class ButtonId(Enum):
    BACK = 0
    PLAY = 1
    SETTINGS = 2
    SCORES = 3
    ABOUT = 4
    HELP = 5
    SOUND_ON = 6
    SOUND_OFF = 7
    CONTROLS = 8
    GALAXIAN = 9
    RACING = 10
    SNAKE = 11
    EASY = 12
    MEDIUM = 13
    HARD = 14
    ENTER_GAME = 15
    EXIT = 16


class PageId(Enum):
    DEFAULT = 0
    PLAY = 1
    SETTINGS = 2
    SCORES = 3
    ABOUT = 4
    HELP = 5
    EXIT = 6


class Menu:
    def __init__(self):
        # TODO sk: Remove below 4 lines and load scores from DB
        snake1 = "1053 points Seba"
        snake2 = "900 points Kuba"
        snake3 = "123 points Mati"
        text_area_lines = ["Galaxian:", snake1, snake2, snake3,
                           "Racing:", snake1, snake2, snake3,
                           "Snake:", snake1, snake2, snake3]

        self._pages = {
            PageId.DEFAULT: Page(header="Raspgierry PI",
                                 buttons=[(ButtonType.TEXT_WIDE, (ButtonId.PLAY, "PLAY")),
                                          (ButtonType.TEXT_WIDE, (ButtonId.SETTINGS, "SETTINGS")),
                                          (ButtonType.TEXT_WIDE, (ButtonId.SCORES, "SCORES")),
                                          (ButtonType.TEXT_WIDE, (ButtonId.EXIT, "EXIT")),
                                          (ButtonType.TEXT_NARROW, (ButtonId.ABOUT, "ABOUT")),
                                          (ButtonType.TEXT_NARROW, (ButtonId.HELP, "HELP"))]),
            PageId.PLAY: Page(header="PLAY",
                              buttons=[(ButtonType.MULTI_CHOICE_LONG,
                                        (None, {ButtonId.GALAXIAN: "GALAXIAN", ButtonId.RACING: "RACING",
                                                ButtonId.SNAKE: "SNAKE"})),
                                       (ButtonType.MULTI_CHOICE_SHORT,
                                        (None, {ButtonId.EASY: "EASY", ButtonId.MEDIUM: "MEDIUM",
                                                ButtonId.HARD: "HARD"})),
                                       (ButtonType.TEXT_NARROW, (ButtonId.BACK, "BACK")),
                                       (ButtonType.TEXT_NARROW, (ButtonId.ENTER_GAME, "PLAY"))]),
            PageId.SETTINGS: Page(header="SETTINGS",
                                  buttons=[(ButtonType.MULTI_CHOICE_SHORT,
                                            (None, {ButtonId.SOUND_ON: "SOUND ON", ButtonId.SOUND_OFF: "SOUND OFF"})),
                                           (ButtonType.TEXT_WIDE, (ButtonId.BACK, "BACK"))]),
            PageId.SCORES: Page(header="BEST SCORES",
                                buttons=[(ButtonType.TEXT_AREA, (ButtonId.HARD, text_area_lines)),
                                         (ButtonType.TEXT_WIDE, (ButtonId.BACK, "BACK"))]),
            PageId.ABOUT: Page(header="CREDITS",
                               buttons=[(ButtonType.TEXT_AREA,
                                         (ButtonId.HARD, ["Jakub Gros", "Sebastian Kucharzyk", "Mateusz Olejarz"])),
                                        (ButtonType.TEXT_WIDE, (ButtonId.BACK, "BACK"))]),
            PageId.HELP: Page(header="HELP",
                              buttons=[(ButtonType.TEXT_AREA,
                                        (ButtonId.HARD, ["Go left: left arrow", "Go right: right arrow",
                                                         "Go up: up arrow", "Go down: down arrow", "Action: A button"])),
                                       (ButtonType.TEXT_WIDE, (ButtonId.BACK, "BACK"))]),
        }
        self._is_moving = DotDict({"up": False, "down": False, "left": False, "right": False, "into": False})
        self._settings = Settings()
        self._active_page_id = PageId.DEFAULT
        self._is_running = True
        self._current_game = None

    def process_events(self, joystick):
        for event in pygame.event.get():
            # TODO sk: remove these lines when game ready
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                sys.exit(0)

            if event.type in {JOYBUTTONUP, JOYBUTTONDOWN, JOYAXISMOTION}:
                joystick.process_event(event)
                if joystick.is_a_pressed():
                    self.get_into()
                if joystick.is_arrow_downdir_pressed():
                    self.move_down()
                if joystick.is_arrow_updir_pressed():
                    self.move_up()
                if joystick.is_arrow_rightdir_pressed():
                    self.move_right()
                if joystick.is_arrow_leftdir_pressed():
                    self.move_left()

    def is_running(self):
        return self._is_running

    def move_up(self):
        self._is_moving.up = True

    def move_down(self):
        self._is_moving.down = True

    def move_left(self):
        self._is_moving.left = True

    def move_right(self):
        self._is_moving.right = True

    def get_into(self):
        self._is_moving.into = True

    def update(self):
        if self._is_moving.up:
            self._update_moving_up()
        elif self._is_moving.down:
            self._update_moving_down()
        elif self._is_moving.left:
            self._update_moving_left()
        elif self._is_moving.right:
            self._update_moving_right()
        elif self._is_moving.into:
            self._update_moving_into()

    def _update_moving_up(self):
        self._pages[self._active_page_id].move_up()
        self._play_sound_and_end_movement(SoundRsc.button_switch, "up")

    def _update_moving_down(self):
        self._pages[self._active_page_id].move_down()
        self._play_sound_and_end_movement(SoundRsc.button_switch, "down")

    def _update_moving_left(self):
        self._pages[self._active_page_id].move_left()
        self._update_settings_if_needed()
        self._play_sound_and_end_movement(SoundRsc.button_switch, "left")

    def _update_moving_right(self):
        self._pages[self._active_page_id].move_right()
        self._update_settings_if_needed()
        self._play_sound_and_end_movement(SoundRsc.button_switch, "right")

    def _play_sound_and_end_movement(self, sound, direction):
        self._play_sound_if_enabled(sound)
        self._is_moving[direction] = False

    def _update_settings_if_needed(self):
        if self._active_page_id == PageId.SETTINGS or self._active_page_id == PageId.PLAY:
            self._update_settings()

    def _update_moving_into(self):
        active_button_id = self._pages[self._active_page_id].get_current_button_id()
        if active_button_id == ButtonId.BACK:
            self._pages[self._active_page_id].reset_current_button()
            self._active_page_id = PageId.DEFAULT
        elif self._active_page_id == PageId.DEFAULT:
            if active_button_id == ButtonId.PLAY:
                self._active_page_id = PageId.PLAY
            elif active_button_id == ButtonId.SETTINGS:
                self._active_page_id = PageId.SETTINGS
            elif active_button_id == ButtonId.SCORES:
                self._active_page_id = PageId.SCORES
            elif active_button_id == ButtonId.EXIT:
                self._is_running = False
            elif active_button_id == ButtonId.ABOUT:
                self._active_page_id = PageId.ABOUT
            elif active_button_id == ButtonId.HELP:
                self._active_page_id = PageId.HELP
        elif self._active_page_id == PageId.PLAY:
            if active_button_id == ButtonId.ENTER_GAME:
                if self._settings.game_type == GameType.Galaxian:
                    self._current_game = Galaxian(self._settings.game_level, self._settings.is_sound_on)
                elif self._settings.game_type == GameType.Racing:
                    self._current_game = Racing(self._settings.game_level, self._settings.is_sound_on)
                elif self._settings.game_type == GameType.Snake:
                    self._current_game = Snake(self._settings.game_level, self._settings.is_sound_on)
                else:
                    raise NotImplementedError("There is no game for " + str(self._settings.game_type))
                self._is_running = False
        self._play_sound_and_end_movement(SoundRsc.button_click, "into")

    def get_current_game(self):
        return self._current_game

    def _update_settings(self):
        choices = self._pages[self._active_page_id].get_active_choices()
        if ButtonId.SOUND_ON in choices:
            self._settings.is_sound_on = True
        elif ButtonId.SOUND_OFF in choices:
            self._settings.is_sound_on = False

        if ButtonId.GALAXIAN in choices:
            self._settings.game_type = GameType.Galaxian
        elif ButtonId.RACING in choices:
            self._settings.game_type = GameType.Racing
        elif ButtonId.SNAKE in choices:
            self._settings.game_type = GameType.Snake

        if ButtonId.EASY in choices:
            self._settings.Level = GameLevel.Easy
        elif ButtonId.MEDIUM in choices:
            self._settings.Level = GameLevel.Medium
        if ButtonId.HARD in choices:
            self._settings.Level = GameLevel.Hard

    def render(self, window):
        self._pages[self._active_page_id].render(window)
        pygame.display.update()

    def _play_sound_if_enabled(self, sound):
        if self._settings.is_sound_on:
            sound.play()
