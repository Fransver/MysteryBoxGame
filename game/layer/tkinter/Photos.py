from tkinter import *
from PIL import ImageTk, Image


def start_photo(root):
    start_img = ImageTk.PhotoImage(Image.open("D:/Pycharm/HandTrackingFrans/game/layer/tkinterimg/box.jpg").resize(size=(400, 320)))
    start_img_label = Label(root, image=start_img)
    start_img_label.photo = start_img  # verankeren foto met .photo
    start_img_label.place(x=200, y=250)
    return start_img_label
