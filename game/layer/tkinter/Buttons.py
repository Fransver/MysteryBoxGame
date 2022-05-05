from tkinter import *


# Lambda is anonieme functie om een actie door te geven

# =========================== Class HomeButton
class HomeButton:
    def __init__(self, root):
        self.quit_button = Button(root, text="Home", fg='blue', width=12, height=3, font=4, command=...)
        self.quit_button.place(x=30, y=510)


# =========================== Class ResetButton

class ResetButton:
    def __init__(self, root, game):
        self.button_reset = Button(root, text="Reset", width=12, height=3, font=4, command=game)
        self.button_reset.place(x=670, y=510)

    def remove_reset_button(self):
        self.button_reset.destroy()


# =========================== Class CameraGameButton


class CameraGameButton:
    def __init__(self, root):
        self.button_camera = Button(root, text="CameraGame", font=4, height=3, width=12, fg='blue')
        self.button_camera.place(x=670, y=510)

    def remove_start_button(self):
        self.button_camera.destroy()


# =========================== Class SoundGameButton

class SoundGameButton:
    def __init__(self, root):
        self.button_sound = Button(root, text="SoundGame", font=4, height=3, width=12, fg='blue', command=lambda:
                                   print("lambda test"))
        self.button_sound.place(x=670, y=400)

    def remove_start_button(self):
        self.button_sound.destroy()


# =========================== Class NameButton

class NameButton:
    def __init__(self, root):
        self.button_name = Button(root, text="Send", fg='blue', width=12, height=3, font=4)
        self.button_name.place(x=670, y=20)

    def remove_namebutton(self):
        self.button_name.destroy()


# =========================== Class QuitButton

class QuitButton:
    def __init__(self, root):
        self.quit_button = Button(root, text="Quit", fg='blue', width=12, height=3, font=4, command=root.destroy)
        self.quit_button.place(x=30, y=510)

    def remove_quit_button(self):
        self.quit_button.destroy()


# =========================== Class InputButton

class InputButton:
    def __init__(self, root, code_print):
        self.input_button = Button(root, text="Send", fg='blue', width=12, height=3, font=4, command=lambda:
                                   print(str(code_print))) # Hoe code gebruiken input?
        self.input_button.place(x=670, y=310)


# =========================== Class NextLevel

class NextLevelButton:
    def __init__(self, root):
        self.next_level = Button(root, text="Next Level", fg='blue', width=12, height=3, font=4, command=lambda :
                                 print("play a harder level of the game, for example, "
                                       "more numbers in the same time"))
        self.next_level.place(x=670, y=220)
