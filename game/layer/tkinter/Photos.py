from tkinter import *
from PIL import ImageTk, Image


def start_photo(root):
    start_img = ImageTk.PhotoImage(Image.open("D:/Pycharm\HandTrackingFrans/andereSpellen/images/tkinterimg/"
                                              "box.jpg").resize(size=(300, 300)))
    start_img_label = Label(root, image=start_img)
    start_img_label.place(x=200, y=200)
