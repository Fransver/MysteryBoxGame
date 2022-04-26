from tkinter import *
from PIL import ImageTk, Image


class StartPhoto:
    def __init__(self, root):
        self.start_img = ImageTk.PhotoImage(Image.open("D:/Pycharm/HandTrackingFrans/game/layer/tkinterimg/box.jpg").resize(size=(400, 320)))
        start_img = self.start_img
        self.start_img_label = Label(root, image=start_img)
        self.start_img_label.photo = start_img  # verankeren foto met .photo
        self.start_img_label.place(x=200, y=250)
