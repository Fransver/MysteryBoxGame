import pygame
from pygame import mixer

# TODO werkend krijgen geluid

pygame.init()


def play_fail_sound():
    fail_sound = pygame.mixer.Sound("layer/sound/Sounds/220191__gameaudio__space-swoosh-brighter.wav")
    fail_sound.play()


class Sound:
    def __init__(self):
        self.fail_sound = play_fail_sound


if __name__ == '__main__':
    Sound()
