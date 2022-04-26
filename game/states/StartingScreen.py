from CameraGameStateMain import *
import tkinter as tk
from game.layer.tkinter.Buttons import *
from game.layer.tkinter.Labels import *
from game.layer.tkinter.Photos import *


class Window(tk.Tk):
    def __init__(self):
        # ====================================== Scherm creëren
        super().__init__()
        self.title('MysteryBox Starting Screen')
        self.geometry('800x600+50+50')
        self.configure(background="steel blue")

        # Labels
        self.home_label = HomeLabel(root=self)

        # Buttons
        # self.name_button = NameButton(root=self)
        self.start_button = StartButton(root=self, game=CameraGame)
        self.quit_button = QuitButton(root=self)

        # Photo
        self.start_photo = StartPhoto(root=self)

    def update_fail(self):
        self.configure(background='red')
        self.title("fail fail fail")
        self.home_label.update_tryagain()


if __name__ == '__main__':  # Testing Starting Window
    start_window = Window()
    start_window.update_fail()
    start_window.mainloop()  # Main Loop runt het scherm
