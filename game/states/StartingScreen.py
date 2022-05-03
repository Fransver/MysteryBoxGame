import tkinter as tk

from states.CameraGame import *
from game.layer.tkinter.Buttons import *
from game.layer.tkinter.Labels import *
from game.layer.tkinter.Photos import *
from game.layer.tkinter.Input import *


# TODO: Hoe kan ik werken met de score uit de game om schermen te updaten??
# TODO: Verder ontwikkelen van reset, complete en fail scherm.


class Window(tk.Tk):

    def __init__(self, spel):
        # ====================================== Scherm creëren
        super().__init__()

        self.title('MysteryBox Starting Screen')
        self.geometry('800x600+50+50')
        self.configure(background="steel blue")

        # Entry
        self.code_input = Input(root=self)

        # Labels
        self.home_label = HomeLabel(root=self)

        # Buttons
        self.camera_game_button = CameraGameButton(root=self, game=spel)
        self.sound_game_button = SoundGameButton(root=self)
        self.quit_button = QuitButton(root=self)
        self.input_button = InputButton(root=self, code_print=self.code_input.e.get()) # <----gebruiken invoer blank
        self.next_button = NextLevelButton(root=self)

        # Photo
        self.start_photo = StartPhoto(root=self)

    def update_fail(self):  # Ga deze waarschijnlijk niet gebruiken en hou het startscherm origineel
        self.configure(background='red')
        self.title("fail fail fail")
        self.home_label.update_tryagain()


if __name__ == '__main__':  # Testing Starting Window
    game = CameraGame().game
    start_window = Window(spel=game)
    start_window.mainloop()
    print("buiten mainloop")
    quit()
