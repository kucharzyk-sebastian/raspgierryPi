import pygame.time


class Sound:
    @staticmethod
    def play_and_wait(sound, delay_ms=185):
        sound.play()
        pygame.time.wait(delay_ms)
