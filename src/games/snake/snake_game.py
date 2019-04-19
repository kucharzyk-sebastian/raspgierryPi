from src.resources.sound_rsc import *
from src.games.game import *
from src.controls.joystick import *
from src.settings import GameLevel
from src.games.snake.board import *
from src.games.snake.snake import *

class SnakeGame(Game):

    SPEEDS = {GameLevel.Easy: 0.5, GameLevel.Medium: 0.3, GameLevel.Hard: 0.1}
    def __init__(self, level, is_sound_on):
        Game.__init__(self, level, is_sound_on)
        self._board = Board(LayoutRsc.GAME_AREA_WIDTH, LayoutRsc.GAME_AREA_HEIGHT, 20, 20)
        self._snake = Snake(SnakeGame.SPEEDS[self._level], self._board)
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
        window.blit(self._board.get_fruit().image, self._board.get_fruit().rect)


    def is_running(self):
        return self._is_running

    def get_points(self):  # TODO jagros: it's confusing, should be scoree
        return self._points

    def get_lives(self):
        return self._lives
