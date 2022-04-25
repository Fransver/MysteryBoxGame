from tkinter import *
from PIL import ImageTk, Image


def start_photo(root):
    start_img = ImageTk.PhotoImage(Image.open("C:/Users/frans.verberne/PycharmProjects/handtrackingfrans"
                                              "/andereSpellen/images/tkinterimg/"
                                              "mysterious-box-agile.gif").resize(size=(300, 300)))
    start_img_label = Label(root, image=start_img)
    start_img_label.place(relx=0.5, rely= 0.5, anchor=CENTER)
    return start_img_label

# label
# gimp
# Alles op 1 scherm heeft de voorkeur.