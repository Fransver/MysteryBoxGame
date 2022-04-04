import cv2
import keyboard

frame = None


def keypresstestq():

    while True:
        if keyboard.is_pressed('q'):
            cv2.rectangle(frame, pt1=(150, 150), pt2=(100, 100), color=(0, 255, 0), thickness=-1)
            print("test succes")

