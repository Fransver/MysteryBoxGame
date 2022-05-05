import tkinter as tk

from game.layer.tkinter.Buttons import *
from game.layer.tkinter.LevelButtons import *
from game.layer.tkinter.Labels import *
from game.layer.tkinter.Photos import *
from game.layer.tkinter.Input import *


class Window(tk.Tk):

    def __init__(self):  # spel meegeven in de app
        # ====================================== Scherm creëren
        super().__init__()
        self.title('MysteryBox Starting Screen')
        self.geometry('800x600+50+50')
        self.configure(background="steel blue")

        # Entry
        self.code_input = Input(root=self)

        # Labels
        self.home_label = HomeLabel(root=self)
        self.game_label = Gamelabel(root=self)

        # Buttons
        self.sound_game_button = SoundGameButton(root=self)
        self.quit_button = QuitButton(root=self)
        self.input_button = InputButton(root=self, code_print=self.code_input.e.get())  # <----gebruiken invoer blank
        self.next_button = NextLevelButton(root=self)

        self.level_1_button = LevelEasyButton(root=self)
        self.level_2_button = LevelMediumButton(root=self)
        self.level_3_button = LevelHardButton(root=self)

        # Photo
        self.start_photo = StartPhoto(root=self)

    def update_fail(self):  # Ga deze waarschijnlijk niet gebruiken en hou het startscherm origineel
        self.configure(background='red')
        self.title("fail fail fail")
        self.home_label.update_tryagain()


if __name__ == '__main__':  # Testing Starting Window
    start_window = Window()
    start_window.mainloop()
    print("buiten mainloop")
    quit()
