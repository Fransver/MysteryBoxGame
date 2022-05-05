from tkinter import *
from game.games.CameraGameMedium import *
from game.games.CameraEasy import *


class LevelEasyButton:
    def __init__(self, root):
        self.level_easy_button = Button(root, text="Easy", fg='blue', width=12, height=3, font=4, command=lambda:
        CameraGameEasy().game(timer=TimeGame().seconds))
        self.level_easy_button.place(x=30, y=400)

    def remove_level_1_button(self):
        self.level_easy_button.destroy()


class LevelMediumButton:
    def __init__(self, root):
        self.level_medium_button = Button(root, text="Medium", fg='blue', width=12, height=3, font=4, command=lambda:
        CameraGameMedium().game(timer=TimeGame().seconds_level_2))
        self.level_medium_button.place(x=30, y=310)

    def remove_level_2_button(self):
        self.level_medium_button.destroy()


class LevelHardButton:
    def __init__(self, root):
        self.level_medium_button = Button(root, text="Hard", fg='blue', width=12, height=3, font=4,
                                          command=lambda:
                                          print("not ready"))
        self.level_medium_button.place(x=30, y=220)

    def remove_level_2_button(self):
        self.level_medium_button.destroy()
