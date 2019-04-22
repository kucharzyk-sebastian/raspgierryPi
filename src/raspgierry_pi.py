from src.gui.menu import *
from src.gui.hud import *
from src.helpers.files import *


class RaspgierryPi:
    MILLISECOND = 1000
    SCORES_DB_PATH = "../scores"
    SCORES_DB_FILENAME = "scores"
    TIME_PER_FRAME = 0.1 * MILLISECOND

    def __init__(self):
        pygame.init()
        self._window = pygame.display.set_mode((LayoutRsc.WINDOW_WIDTH,  LayoutRsc.WINDOW_HEIGHT), FULLSCREEN)
        pygame.display.set_caption('Raspgierry Pi')
        try:
            self._joystick = Joystick(0)
        except pygame.error:
            print("Couldn't detect valid joystick")
            sys.exit(1)
        try:
            self._scores = Files.load_obj(RaspgierryPi.SCORES_DB_PATH, RaspgierryPi.SCORES_DB_FILENAME)
        except FileNotFoundError:
            self._scores = {GameType.Galaxian: [0, 0, 0], GameType.Racing: [0, 0, 0], GameType.Snake: [0, 0, 0]}
        self._menu = Menu(self._scores)
        self._clock = pygame.time.Clock()
        self._is_running = True

    def run(self):
        while self._is_running:
            time_since_last_update = 0

            while self._menu.is_running():
                self._menu.process_events(self._joystick)
                time_since_last_update += self._clock.tick()
                while time_since_last_update >= RaspgierryPi.TIME_PER_FRAME:
                    time_since_last_update -= RaspgierryPi.TIME_PER_FRAME
                    self._menu.process_events(self._joystick)
                    self._menu.update()
                self._menu.render(self._window)

            game = self._menu.get_current_game()
            if game:
                hud = Hud(game)
                hud.render(self._window)
                while hud.is_running():
                    hud.process_events(self._joystick)
                    time_since_last_update += self._clock.tick()
                    while time_since_last_update >= RaspgierryPi.TIME_PER_FRAME:
                        time_since_last_update -= RaspgierryPi.TIME_PER_FRAME
                        hud.process_events(self._joystick)
                        hud.update(RaspgierryPi.TIME_PER_FRAME * 0.001)  # convert to seconds
                    hud.render(self._window)
                self.update_stats(game)
                self._is_running = True
                self.__init__()
            else:
                self._is_running = False

    def update_stats(self, game):
        scores = self._scores[game.get_type()]
        for i in range(len(scores)):
            if game.get_points() > scores[i]:
                scores.insert(i, game.get_points())
                break
        Files.save_obj(RaspgierryPi.SCORES_DB_PATH, self._scores, RaspgierryPi.SCORES_DB_FILENAME)
