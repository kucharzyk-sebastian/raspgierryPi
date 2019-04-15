from src.gui.menu import *
from src.gui.hud import *
from src.controls.joystick import *
from src.gui.indented_rect import *

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
            hud = Hud()
            hud.draw(self._window)
            self._window.fill(LayoutRsc.WINDOW_COLOR)
            game_view = pygame.Surface((300, 370))
            game_view.fill((255, 255, 255))
            while game.is_running():
                game.process_events(self._joystick)
                time_since_last_update += self._clock.tick()
                while time_since_last_update > self._time_per_frame:
                    time_since_last_update -= self._time_per_frame
                    game.process_events(self._joystick)
                    game.update(self._time_per_frame)
                hud.draw(self._window)
                game.render(self._window)
