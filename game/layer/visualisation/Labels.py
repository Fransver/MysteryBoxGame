from tkinter import *


class HomeLabel:
    def __init__(self, root):
        self.var = StringVar()
        self.var.set("Mystery Box")
        self.home_label = Label(root, textvariable=self.var, font='Aerial 25 bold italic', border=5,
                                fg ='#6321BF', background="#E3E1C6", relief=SUNKEN, width=20, height=2)
        self.home_label.pack(pady=30)

    def remove_home_label(self):
        self.home_label.destroy()

    def update_tryagain(self):
        self.var.set("Try Again")

    def update_complete(self):
        self.var.set("Complete!")


class Gamelabel:
    def __init__(self, root):
        self.var = StringVar()
        self.var.set("Camera Game")
        self.home_label = Label(root, textvariable=self.var, font='Aerial 20 bold italic', fg='#6321BF',
                                relief=SUNKEN, padx=2, border=5, width=20, background="#E3E1C6", height=1)
        self.home_label.place(relx=0.28, rely=0.28)