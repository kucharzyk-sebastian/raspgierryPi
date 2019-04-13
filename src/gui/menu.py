import sys
from src.gui.page import *
from src.settings import *
from src.helpers.dotdict import *
from src.helpers.sound import *
from src.resources.sound_rsc import *
from enum import Enum


class ButtonId(Enum):
    Back = 0
    Play = 1
    Settings = 2
    Scores = 3
    About = 4
    Help = 5
    SoundOn = 6
    SoundOff = 7
    Controls = 8
    Galaxian = 9
    Racing = 10
    Snake = 11
    Easy = 12
    Medium = 13
    Hard = 14
    EnterGame = 15
    Exit = 16


class PageId(Enum):
    Default = 0
    Play = 1
    Settings = 2
    Scores = 3
    About = 4
    Help = 5
    Exit = 6


class Menu:
    def __init__(self):
        # TODO sk: Remove below 4 lines and load scores from DB
        snake1 = "1053 points Seba"
        snake2 = "900 points Kuba"
        snake3 = "123 points Mati"
        text_area_lines = ["Galaxian:", snake1, snake2, snake3, "Racing:", snake1, snake2, snake3, "Snake:", snake1, snake2, snake3]

        self._pages = {
            PageId.Default: Page(header="Raspgierry PI",
                                 buttons=[(ButtonType.TextWide, (ButtonId.Play, "PLAY")),
                                          (ButtonType.TextWide, (ButtonId.Settings, "SETTINGS")),
                                          (ButtonType.TextWide, (ButtonId.Scores, "SCORES")),
                                          (ButtonType.TextWide, (ButtonId.Exit, "EXIT")),
                                          (ButtonType.TextNarrow, (ButtonId.About, "ABOUT")),
                                          (ButtonType.TextNarrow, (ButtonId.Help, "HELP"))]),
            PageId.Play: Page(header="PLAY",
                              buttons=[(ButtonType.MultiChoiceLong, (None, {ButtonId.Galaxian: "GALAXIAN", ButtonId.Racing: "RACING", ButtonId.Snake: "SNAKE"})),
                                       (ButtonType.MultiChoiceShort, (None, {ButtonId.Easy: "EASY", ButtonId.Medium: "MEDIUM", ButtonId.Hard: "HARD"})),
                                       (ButtonType.TextNarrow, (ButtonId.Back, "BACK")),
                                       (ButtonType.TextNarrow, (ButtonId.EnterGame, "PLAY"))]),
            PageId.Settings: Page(header="SETTINGS",
                                  buttons=[(ButtonType.MultiChoiceShort, (None, {ButtonId.SoundOn: "SOUND ON", ButtonId.SoundOff: "SOUND OFF"})),
                                           (ButtonType.TextWide, (ButtonId.Back, "BACK"))]),
            PageId.Scores: Page(header="BEST SCORES",
                                # TODO sk: remove hardcoded button Id
                                buttons=[(ButtonType.TextArea, (ButtonId.Hard, text_area_lines)),
                                         (ButtonType.TextWide, (ButtonId.Back, "BACK"))]),
            PageId.About: Page(header="CREDITS",
                               buttons=[(ButtonType.TextArea, (ButtonId.Hard, ["Jakub Gros", "Sebastian Kucharzyk", "Mateusz Olejarz"])),
                                        (ButtonType.TextWide, (ButtonId.Back, "BACK"))]),
            PageId.Help: Page(header="HELP",
                              buttons=[(ButtonType.TextArea, (ButtonId.Hard, ["Go left: left arrow", "Go right: right arrow", "Go up: up arrow", "Go down: down arrow", "Action: A button"])),
                                       (ButtonType.TextWide, (ButtonId.Back, "BACK"))]),
        }
        self._is_moving = dotdict({"up": False, "down": False, "left": False, "right": False, "into": False})
        self._settings = Settings()
        self._active_page_id = PageId.Default

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
            self._pages[self._active_page_id].move_up()
            play_and_wait(SoundRsc.button_switch)
            self._is_moving.up = False
        elif self._is_moving.down:
            self._pages[self._active_page_id].move_down()
            play_and_wait(SoundRsc.button_switch)
            self._is_moving.down = False
        elif self._is_moving.left:
            self._pages[self._active_page_id].move_left()
            if self._active_page_id == PageId.Settings or self._active_page_id == PageId.Play:
                self.update_settings()
            play_and_wait(SoundRsc.button_switch)
            self._is_moving.left = False
        elif self._is_moving.right:
            self._pages[self._active_page_id].move_right()
            if self._active_page_id == PageId.Settings or self._active_page_id == PageId.Play:
                self.update_settings()
            play_and_wait(SoundRsc.button_switch)
            self._is_moving.right = False
        elif self._is_moving.into:
            active_button_id = self._pages[self._active_page_id].get_current_button_id()
            if active_button_id == ButtonId.Back:
                self._pages[self._active_page_id].reset_current_button()
                self._active_page_id = PageId.Default
            elif self._active_page_id == PageId.Default:
                if active_button_id == ButtonId.Play:
                    self._active_page_id = PageId.Play
                elif active_button_id == ButtonId.Settings:
                    self._active_page_id = PageId.Settings
                elif active_button_id == ButtonId.Scores:
                    self._active_page_id = PageId.Scores
                elif active_button_id == ButtonId.Exit:
                    # TODO sk: change way of quitting
                    sys.exit(0)
                elif active_button_id == ButtonId.About:
                    self._active_page_id = PageId.About
                elif active_button_id == ButtonId.Help:
                    self._active_page_id = PageId.Help
            elif self._active_page_id == PageId.Play:
                print(active_button_id)
                if active_button_id == ButtonId.EnterGame:
                    # TODO sk: remove when game page will be ready
                    pass
            play_and_wait(SoundRsc.button_click)
            self._is_moving.into = False

    def update_settings(self):
        choices = self._pages[self._active_page_id].get_active_choices()
        if ButtonId.SoundOn in choices:
            self._settings.SoundOn = True
        elif ButtonId.SoundOff in choices:
            self._settings.SoundOn = False

        if ButtonId.Galaxian in choices:
            self._settings.Game = Game.Galaxian
        elif ButtonId.Racing in choices:
            self._settings.Game = Game.Racing
        elif ButtonId.Snake in choices:
            self._settings.Game = Game.Snake

        if ButtonId.Easy in choices:
            self._settings.Level = GameLevel.Easy
        elif ButtonId.Medium in choices:
            self._settings.Level = GameLevel.Medium
        if ButtonId.Hard in choices:
            self._settings.Level = GameLevel.Hard

    def render(self, window):
        self._pages[self._active_page_id].render(window)
