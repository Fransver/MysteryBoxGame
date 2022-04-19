import tkinter as tk
from game.layer.tkinter.Buttons import *
from game.layer.tkinter.Labels import *


def window_complete():
    root = tk.Tk()
    root.title("Complete Screen test")
    root.geometry('600x400+50+50')

    label_complete(root)
    quit_button(root)

    root.mainloop()


if __name__ == '__main__':
    window_complete()
