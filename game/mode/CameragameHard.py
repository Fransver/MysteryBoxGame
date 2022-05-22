from game.mode import CameraEasy
from game.commands import LevelTimer


class CameraGameHard(CameraEasy.CameraGameEasy):
    def __int__(self):
        super().__init__()


if __name__ == '__main__':
    game = CameraGameHard()
    game.game(timer=LevelTimer.TimeGame().seconds_level_3)
