from tkinter import *


def start_button(root):
    button_home = Button(root, text="Start", font=4, height=3, width=10, fg='blue', command=root.destroy)
    button_home.place(x=670, y=510)


def quit_button(root):
    button_home = Button(root, text="Quit", fg='blue', width=10, height=3, font=4, command=root.destroy)
    button_home.place(x=30, y=510)


class NameButton:
    def __init__(self, root):
        self.button_name = Button(root, text="Send", fg='blue')
        self.button_name.place(x=380, y=130)

    def remove_namebutton(self):
        self.button_name.destroy()
