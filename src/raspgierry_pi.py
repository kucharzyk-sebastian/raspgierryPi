from src.gui.menu import *
from src.gui.hud import *


class RaspgierryPi:
    TIME_PER_FRAME = 0.1 * 1000 #TODO jagros: what does those values means

    def __init__(self):
        pygame.init()
        self._window = pygame.display.set_mode((LayoutRsc.WINDOW_WIDTH,  LayoutRsc.WINDOW_HEIGHT), RESIZABLE)
        pygame.display.set_caption('Raspgierry Pi')
        try:
            self._joystick = Joystick(0)
        except pygame.error:
            print("Couldn't detect valid joystick")
            sys.exit(1)
        self._menu = Menu()
        self._clock = pygame.time.Clock()
        
    def run(self):
        time_since_last_update = 0

        while self._menu.is_running():
            self._menu.process_events(self._joystick)
            time_since_last_update += self._clock.tick()
            while time_since_last_update >= RaspgierryPi.TIME_PER_FRAME:
                time_since_last_update -= RaspgierryPi.TIME_PER_FRAME
                self._menu.process_events(self._joystick)
                self._menu.update()
            self._menu.render(self._window)

        game = SnakeGame(GameLevel.Hard, True) #self._menu.get_current_game()
        if game:
            hud = Hud(game)
            hud.render(self._window)
            while hud.is_running():
                hud.process_events(self._joystick)
                time_since_last_update += self._clock.tick()
                while time_since_last_update >= RaspgierryPi.TIME_PER_FRAME:
                    time_since_last_update -= RaspgierryPi.TIME_PER_FRAME
                    hud.process_events(self._joystick)
                    hud.update(RaspgierryPi.TIME_PER_FRAME * 0.001) #TODO jagros why 0.001
                hud.render(self._window)
