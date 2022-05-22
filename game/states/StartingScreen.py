import tkinter as tk

from game.layer.tkinter.Buttons import *
from game.layer.tkinter.LevelButtons import *
from game.layer.tkinter.Labels import *
from game.layer.tkinter.Photos import *



class Window(tk.Tk):

    def __init__(self):  # spel meegeven in de app
        # ====================================== Scherm creëren
        super().__init__()
        self.title('MysteryBox Starting Screen')
        self.geometry('800x600+50+50')
        self.configure(background="#A67538")

        # Entry
        # self.code_input = Input(root=self)

        # Labels
        self.home_label = HomeLabel(root=self)
        self.game_label = Gamelabel(root=self)

        # Buttons
        # self.sound_game_button = SoundGameButton(root=self)
        self.explain_button = ExplanationButton(root=self)
        self.quit_button = QuitButton(root=self)
        # self.input_button = InputButton(root=self, code_print=self.code_input.e.get())  # <----gebruiken invoer blank

        self.level_1_button = LevelEasyButton(root=self)
        self.level_2_button = LevelMediumButton(root=self)
        self.level_3_button = LevelHardButton(root=self)

        self.lmain = Label(self)
        self.lmain.place(x=200, y=250)

        # Photo
        self.start_photo = StartPhoto(root=self)

    def update_fail(self):  # Ga deze waarschijnlijk niet gebruiken en hou het startscherm origineel
        self.configure(background='red')
        self.title("fail fail fail")
        self.home_label.update_tryagain()

    # function for video streaming
    # def video_stream(self):
    #     cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    #     _, frame = cam.read()
    #     cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    #     img = Image.fromarray(cv2image)
    #     imgtk = ImageTk.PhotoImage(image=img)
    #     self.lmain.imgtk = imgtk
    #     self.lmain.configure(image=imgtk)
    #     self.lmain.after(1, self.video_stream)


if __name__ == '__main__':  # Testing Starting Window
    start_window = Window()

    start_window.mainloop()
    print("buiten mainloop")
    quit()
