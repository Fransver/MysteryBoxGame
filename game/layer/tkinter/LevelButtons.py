import threading

from tkinter import *
from game.games.CameraGameMedium import *
from game.games.CameraEasy import *
from game.games.CameragameHard import *


# Hier nu de spellen met Lambda doorgegeven aan de knoppen.


def thread_game_easy():
    threading.Thread(CameraGameEasy().game(timer=TimeGame().seconds)).start()


def thread_game_medium():
    threading.Thread(CameraGameMedium().game(timer=TimeGame().seconds_level_2)).start()


def thread_game_hard():
    threading.Thread(CameraGameHard().game(timer=TimeGame().seconds_level_3)).start()


class LevelEasyButton:

    def __init__(self, root):
        self.level_easy_button = Button(root, text="Easy", fg='#6FBF1F', width=8, height=2,
                                        font="Times 15 italic bold",
                                        command=thread_game_easy)
        self.level_easy_button.place(x=30, y=400)

    def remove_level_1_button(self):
        self.level_easy_button.destroy()


class LevelMediumButton:
    def __init__(self, root):
        self.level_medium_button = Button(root, text="Medium", fg='#303473', width=8, height=2,
                                          font="Times 15 italic bold",
                                          command=thread_game_medium)
        self.level_medium_button.place(x=30, y=310)

    def remove_level_2_button(self):
        self.level_medium_button.destroy()


class LevelHardButton:
    def __init__(self, root):
        self.level_medium_button = Button(root, text="Hard", fg='#D9483B', width=8, height=2,
                                          font="Times 15 italic bold",
                                          command=thread_game_hard)
        self.level_medium_button.place(x=30, y=220)

    def remove_level_2_button(self):
        self.level_medium_button.destroy()
