import tkinter as tk

from game.layer.visualisation.Buttons import *
from game.layer.visualisation.LevelButtons import *
from game.layer.visualisation.Labels import *
from game.layer.visualisation.Photos import *


class Window(tk.Tk):

    def __init__(self):  # spel meegeven in de app
        # ====================================== Scherm creëren
        super().__init__()
        self.title('MysteryBox CameraGame')
        self.geometry('800x600+50+50')
        self.configure(background="#A67538")

        # Entry
        # self.code_input = Input(root=self)

        # Labels
        self.home_label = HomeLabel(root=self)
        self.game_label = Gamelabel(root=self)

        # Buttons
        self.explain_button = ExplanationButton(root=self)
        self.quit_button = QuitButton(root=self)

        self.level_1_button = LevelEasyButton(root=self)
        self.level_2_button = LevelMediumButton(root=self)
        self.level_3_button = LevelHardButton(root=self)

        self.lmain = Label(self)
        self.lmain.place(x=200, y=250)

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
