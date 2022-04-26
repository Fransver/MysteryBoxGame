import tkinter as tk
from game.layer.tkinter.Buttons import *
from game.layer.tkinter.Labels import *
from game.layer.tkinter.Entry import *
from game.layer.tkinter.Photos import *


class FailScreen(Tk):
    def __init__(self):
        super().__init__()

        self.geometry('800x600+50+50')
        self.title("fail fail fail")
        self.configure(background='red')

        self.start_photo = StartPhoto(self)

        # Buttons
        self.reset_button = ResetButton(root=self, game=...)

        # Labels
        self.fail_label = HomeLabel(self).update_tryagain()


if __name__ == '__main__':
    fail_screen = FailScreen()
    fail_screen.mainloop()
