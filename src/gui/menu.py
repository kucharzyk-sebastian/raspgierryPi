import sys
from src.helpers.dotdict import *
from src.gui.page import *
from src.gui.multi_choice_button import *

class PageType(Enum):
    Default = 0
    Play = 1
    Settings = 2
    Scores = 3
    About = 4
    Help = 5


class Menu:
    def __init__(self):
        # TODO sk: Remove below 4 lines and load scores from DB
        snake1 = "1053 points Seba"
        snake2 = "900 points Kuba"
        snake3 = "123 points Mati"
        text_area_lines = ["Galaxian:", snake1, snake2, snake3, "Racing:", snake1, snake2, snake3, "Snake:", snake1, snake2, snake3]

        self._pages = {
            PageType.Default: Page(header="Raspgierry PI",
                                   wide_button_labels={ButtonType.Play: "PLAY", ButtonType.Settings: "SETTINGS",
                                                       ButtonType.Scores: "SCORES", ButtonType.Exit: "EXIT"},
                                   narrow_button_labels={ButtonType.About: "ABOUT", ButtonType.Help: "HELP"}),
            PageType.Play: Page(header="GALAXIAN",
                                narrow_button_labels={ButtonType.Back: "BACK", ButtonType.Play: "PLAY"},
                                selectable_area_long=["GALAXIAN", "RACING", "SNAKE"],
                                selectable_area_short=["EASY", "MEDIUM", "HARD"]),
            PageType.Settings: Page(header="SETTINGS",
                                    wide_button_labels={ButtonType.Empty: None, ButtonType.Empty: None,
                                                        ButtonType.Empty:  None, ButtonType.Empty: None,
                                                        ButtonType.Back:  "BACK"},
                                    selectable_area_short=["SOUND ON", "SOUND OFF"]),
            PageType.Scores: Page(header="BEST SCORES",
                                  text_area_lines=text_area_lines,
                                  wide_button_labels={ButtonType.Back: "BACK"}),
            PageType.About: Page(header="CREDITS",
                                 text_area_lines=["Jakub Gros", "Sebastian Kucharzyk", "Mateusz Olejarz"],
                                 wide_button_labels={ButtonType.Back: "BACK"}),
            PageType.Help: Page(header="HELP",
                                text_area_lines=["Go left: left arrow", "Go right: right arrow", "Go up: up arrow", "Go down: down arrow", "Action: A button"],
                                wide_button_labels={ButtonType.Back: "BACK"})
        }
        self._is_moving = dotdict({"up": False, "down": False, "left": False, "right": False })
        self._active_page = PageType.Default

    def move_up(self):
        self._is_moving.up = True

    def move_down(self):
        self._is_moving.down = True

    def move_left(self):
        self._is_moving.left = True

    def move_right(self):
        self._is_moving.right = True

    def get_into(self):
        active_button_type = self._pages[self._active_page].get_chosen_button()
        if active_button_type == ButtonType.Back:
            self._pages[self._active_page].reset_chosen_button()
            self._active_page = PageType.Default
        elif self._active_page == PageType.Default:
            if active_button_type == ButtonType.Play:
                self._active_page = PageType.Play
            elif active_button_type == ButtonType.Settings:
                self._active_page = PageType.Settings
            elif active_button_type == ButtonType.Scores:
                self._active_page = PageType.Scores
            elif active_button_type == ButtonType.Exit:
                # TODO sk: change way of quitting
                sys.exit(0)
            elif active_button_type == ButtonType.About:
                self._active_page = PageType.About
            elif active_button_type == ButtonType.Help:
                self._active_page = PageType.Help

    def update(self):
        if self._is_moving.up:
            self._pages[self._active_page].move_up()
            self._is_moving.up = False
        elif self._is_moving.down:
            self._pages[self._active_page].move_down()
            self._is_moving.down = False
        elif self._is_moving.left:
            self._pages[self._active_page].move_left()
            self._is_moving.left = False
        elif self._is_moving.right:
            self._pages[self._active_page].move_right()
            self._is_moving.right = False


    def render(self, window):
        self._pages[self._active_page].render(window)
