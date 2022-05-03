import tkinter as tk
from game.layer.tkinter.Buttons import *
from game.layer.tkinter.Labels import *
from game.layer.tkinter.Photos import *


class CompleteScreen(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('800x600+50+50')
        self.title("You have won the game!!!")
        self.configure(background='green')

        self.start_photo = StartPhoto(self)

        # Buttons
        self.quit_button = QuitButton(root=self)

        # Labels
        self.title = HomeLabel(self).update_complete()
