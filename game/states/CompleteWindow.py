import tkinter as tk
from game.layer.tkinter.Buttons import *


def window_complete():
    root = tk.Tk()
    root.title("Complete Screen test")
    root.geometry('600x400+50+50')

    home_button(root)


    root.mainloop()


if __name__ == '__main__':
    window_complete()
