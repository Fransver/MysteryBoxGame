import tkinter as tk

# Proberen vanaf hier aan te roepen.
from game.layer.tkinter.Buttons import *
from game.layer.tkinter.Labels import *
from game.layer.tkinter.Entry import *
from game.layer.tkinter.Photos import *


class Window(tk.Tk):
    def __init__(self):
        # ====================================== Scherm creëren
        super().__init__()
        self.title('MysteryBox Starting Screen')
        self.geometry('800x600+50+50')
        self.configure(background="steel blue")

        # Input
        self.input_name = Input(root=self)

        # Labels
        self.home_label = label_home(self)

        # Buttons
        self.start_button = start_button(self)
        self.quit_button = quit_button(self)
        self.name_button = NameButton(root=self)

        # Photo
        self.start_photo = start_photo(self)

    def update_complete(self):
        self.home_label = label_complete(self)

    def end_game(self):
        self.input_name = Input.update_remove_input(self.input_name)
        self.home_label = label_fail(self)
        self.name_button.remove_namebutton()



if __name__ == '__main__':  # Testing Starting Window
    start_window = Window()
    start_window.end_game()
    start_window.mainloop()
