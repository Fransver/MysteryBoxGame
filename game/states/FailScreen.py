import tkinter as tk
from game.layer.tkinter.Buttons import *
from game.layer.tkinter.Labels import *


def window_fail():
    root = tk.Tk()
    root.title("Fail Fail Fail")
    root.geometry('600x400+50+50')
    root.configure(background="red")

    label_fail(root)
    quit_button(root)

    root.mainloop()


if __name__ == '__main__':
    window_fail()
