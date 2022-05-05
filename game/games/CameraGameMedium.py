from game.games import CameraEasy
from game.commands.LevelTimer import *


class CameraGameMedium(CameraEasy.CameraGameEasy):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    game = CameraGameMedium()
    game.game(timer=TimeGame().seconds_level_2)
