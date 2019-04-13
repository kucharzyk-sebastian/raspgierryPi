import pygame.time


def play_and_wait(sound, delay_ms=185):
    sound.play()
    pygame.time.wait(delay_ms)
