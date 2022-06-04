from tkinter import *


class Input:
    def __init__(self, root):
        self.e = Entry(root, width=30, borderwidth=5)  # input gebruiker
        self.e.place(x=300, y=200)


    def update_remove_input(self):
        self.e.destroy()
