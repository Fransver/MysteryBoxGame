from tkinter import *


def label_home(root):
    home_label = Label(root, text="Mystery Box", font='Aerial 17 bold italic')
    home_label.pack(pady=30)
    home_label.configure(background="steel blue")


def label_complete(root):
    complete_label = Label(root, text="Complete !!!", font='Aerial 17 bold italic')
    complete_label.pack(pady=30)
    complete_label.configure(background="steel blue")


def label_fail(root):
    fail_label = Label(root, text="You Failed !!!", font='Aerial 17 bold italic', background="red")
    fail_label.pack(pady=30)
    fail_label.configure(background="steel blue")


def label_start(root):
    start_label = Label(root, text="Mystery Box", font='Aerial 17 bold italic')
    start_label.pack(pady=30)
    start_label.configure(background="steel blue")
