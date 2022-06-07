import os.path
from tkinter import *
from PIL import ImageTk, Image
import os


start_photo = "game/layer/visualisation/tkinterimg/box.jpg"
start_join = os.path.join("tkinterimg", "box.jpg")


class StartPhoto:
    def __init__(self, root):
        self.start_img = ImageTk.PhotoImage(
            Image.open(start_photo).resize(size=(400, 320)))
        start_img = self.start_img
        self.start_img_label = Label(root, image=start_img)
        self.start_img_label.photo = start_img  # verankeren foto met .photo
        self.start_img_label.place(x=200, y=250)
