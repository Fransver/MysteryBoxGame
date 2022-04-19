import sys
import tkinter as tk

from game.layer.tkinter.Buttons import *
from game.layer.tkinter.Labels import *
from game.states.CameraGameStateMain import *

# ====================================== Scherm creëren
root = tk.Tk()

# ====================================== Game selecteren voor startscherm
game = CameraGame  # Niet de functie aanroepen voor de knop command.


def window_start():
    root.title("Start Screen test")
    root.geometry('800x600+50+50')

    start_button(root, game)

    label_home(root)

    root.mainloop()

if __name__ == '__main__':
    window_start()

