from tkinter import *


# Waarom ene knop wel door kunnen geven in class en andere niet??

# =========================== Class ResetButton

class ResetButton:
    def __init__(self, root, game):
        self.button_reset = Button(root, text="Reset", width=10, height=3, font=4, command=game)
        self.button_reset.place(x=670, y=510)

    def remove_reset_button(self):
        self.button_reset.destroy()


# =========================== Class StartButton


class StartButton:
    def __init__(self, root, game):
        self.button_start = Button(root, text="Start", font=4, height=3, width=10, fg='blue', command=game)
        self.button_start.place(x=670, y=510)

    def remove_start_button(self):
        self.button_start.destroy()


# =========================== Class NameButton

class NameButton:
    def __init__(self, root):
        self.button_name = Button(root, text="Send", fg='blue', width=10, height=3, font=4)
        self.button_name.place(x=670, y=20)

    def remove_namebutton(self):
        self.button_name.destroy()


# =========================== Class QuitButton

class QuitButton:
    def __init__(self, root):
        self.quit_button = Button(root, text="Quit", fg='blue', width=10, height=3, font=4, command=root.destroy)
        self.quit_button.place(x=30, y=510)


    def remove_quit_button(self):
        self.quit_button.destroy()
