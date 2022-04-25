import tkinter as tk

from game.layer.tkinter.Buttons import *
from game.layer.tkinter.Labels import *
from game.layer.tkinter.Photos import *

root = tk.Tk()
root.configure(background="steel blue")
e = Entry(root, width=30, borderwidth=5)  # input gebruiker

""""
class Window :
    def __init__(self):
        # ====================================== Scherm creëren
        root = tk.Tk()
        root.configure(background="steel blue")
        e = Entry(root, width=30, borderwidth=5)  # input gebruiker
        
        self.root = root
    def update(self):
        ...
    def end_game(self):
"""
# ====================================== Photo


# ====================================== Game selecteren voor startscherm


def click_name():
    name = e.get()
    nameLabel = Label(root, text=name, font='Aerial 12 bold italic')
    nameLabel.pack()
    nameLabel.configure(background="steel blue")


def name_button():
    button_name = Button(root, text="Send", fg='blue', command=click_name)
    button_name.place(x=390, y=480)


def window_start():
    root.title("Start Screen test")
    root.geometry('800x600+50+50')

    start_photo(root)
    label_home(root)
    start_button(root)
    e.pack()
    click_name()
    name_button()

    root.mainloop()


if __name__ == '__main__':
    window_start()
