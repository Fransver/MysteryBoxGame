import tkinter as tk
import keyboard



def CreateWindow():
    window= tk.Tk()
    # add widgets here
    window.title('Hello Python')
    window.geometry("300x200+10+20")
    window.mainloop()

def InvoerCodeConsole():
    while True:
        if keyboard.is_pressed('q'):
            print("Voer een antwoord in")
            codeInput = int(input())
            print(codeInput)
            break
