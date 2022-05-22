import pygame

pygame.mixer.init()

# TODO werkend krijgen geluid


def play_fail_sound():
    pygame.mixer.music.load("game/layer/pygame/Sounds/fail1.wav")


class Sound:
    def __init__(self):
        self.fail_sound = play_fail_sound
