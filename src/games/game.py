
class Game:
    def __init__(self, level, sound_on):
        self._level = level
        self._sound_on = sound_on
        self._is_running = True

    def process_events(self, joystick):
        pass

    def update(self, delta_time):
        pass

    def render(self, window):
        pass

    def is_running(self):
        return self._is_running
