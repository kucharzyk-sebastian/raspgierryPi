from src.controls.joystick import *
from src.games.game import *
from src.games.snake.board import *
from src.games.snake.player import *
from src.resources.layout_rsc import LayoutRsc
from src.resources.sound_rsc import *
from src.games.snake.settings import SnakeSettings


class Snake(Game):
    def __init__(self, level, is_sound_on, game_type):
        Game.__init__(self, level, is_sound_on, game_type)
        self._board = Board(LayoutRsc.GAME_AREA_WIDTH,
                            LayoutRsc.GAME_AREA_HEIGHT,
                            SnakeSettings.BOARD_FIELDS_HORIZONTALLY,
                            SnakeSettings.BOARD_FIELDS_VERTICALLY)
        self._player = Player(SnakeSettings.SNAKE_SPEEDS[level], self._board, is_sound_on)
        self._lives = 3
        self._is_running = True
        self._points = 0

    def process_events(self, joystick):
        for event in pygame.event.get():
            joystick.process_event(event)

            if event.type in {JOYBUTTONUP, JOYBUTTONDOWN, JOYAXISMOTION}:
                if joystick.is_arrow_updir_pressed():
                    self._player.set_direction("up")
                if joystick.is_arrow_downdir_pressed():
                    self._player.set_direction("down")
                if joystick.is_arrow_leftdir_pressed():
                    self._player.set_direction("left")
                if joystick.is_arrow_rightdir_pressed():
                    self._player.set_direction("right")
                if joystick.is_y_pressed():
                    self._is_running = False

    def update(self, delta_time):
        self._player.update(delta_time)
        self._points = self._player.get_fruits_eaten()

        if self._player.has_collided_with_itself():
            self._die()

        if self._lives == 0:
            self._is_running = False

    def render(self, window):
        window.fill(LayoutRsc.WINDOW_COLOR)
        self._player.draw(window)
        window.blit(self._board.get_fruit().image, self._board.get_fruit().rect)

    def _die(self):
        self._lives -= 1
        self._player.respawn()
