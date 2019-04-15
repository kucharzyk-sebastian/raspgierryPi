from src.gui.menu import *
from src.gui.hud import *


class RaspgierryPi:
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
        self._time_per_frame = 1/60
        self._clock = pygame.time.Clock()
        
    def run(self):
        time_since_last_update = 0
        while self._menu.is_running():
            self._menu.process_events(self._joystick)
            time_since_last_update += self._clock.tick()
            while time_since_last_update > self._time_per_frame:
                time_since_last_update -= self._time_per_frame
                self._menu.process_events(self._joystick)
                self._menu.update()
            self._menu.render(self._window)

        game = self._menu.get_game()
        if game:
            hud = Hud(game)
            hud.render(self._window)
            while hud.is_running():
                hud.process_events(self._joystick)
                time_since_last_update += self._clock.tick()
                while time_since_last_update > self._time_per_frame:
                    time_since_last_update -= self._time_per_frame
                    hud.process_events(self._joystick)
                    hud.update(self._time_per_frame)
                hud.render(self._window)
