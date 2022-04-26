from tkinter import *


class HomeLabel:
    def __init__(self, root):
        self.var = StringVar()
        self.var.set("Mystery Box")
        self.home_label = Label(root, textvariable=self.var, font='Aerial 17 bold italic')
        self.home_label.pack(pady=30)

    def remove_home_label(self):
        self.home_label.destroy()

    def update_tryagain(self):
        self.var.set("Try Again")

    def update_complete(self):
        self.var.set("Complete!")

