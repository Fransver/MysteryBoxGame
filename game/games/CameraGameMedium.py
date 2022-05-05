from games.CameraEasy import CameraGameEasy
from game.commands.LevelTimer import *


class CameraGameMedium(CameraGameEasy):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    game = CameraGameMedium()
    game.game(timer=TimeGame().seconds_level_2)
    quit()
