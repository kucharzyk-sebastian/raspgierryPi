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

    def has_collided_with_itself(self):
        sprites = self._snake.get_occupied_points().sprites()
        body_rect_list = [x.rect for x in sprites]
        head_rect = self._snake.get_head_rect()
        body_rect_list.remove(head_rect)
        return(head_rect.collidelist(body_rect_list) >= 0)

    def update(self, delta_time):
        self._snake.update(delta_time)
        self._points = self._snake.get_snake_size() - 1 #start size of snake is 1
        if self.has_collided_with_itself():
            self._is_running = False



    def render(self, window):
        window.fill(LayoutRsc.WINDOW_COLOR)
        self._snake.draw(window)
        window.blit(self._board.get_fruit().image, self._board.get_fruit().rect)

