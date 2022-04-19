from tkinter import *



def start_button(root):
    button_home = Button(root, text="Start", fg='blue', command=root.destroy)
    button_home.place(x=700, y=550)


def quit_button(root):
    button_home = Button(root, text="Close", fg='red', command=root.destroy)
    button_home.place(x=700, y=550)


def name_button(root):
    button_name = Button(root, text="Send", fg='blue')
    button_name.place(x=400, y=300)







