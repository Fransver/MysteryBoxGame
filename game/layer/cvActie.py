import cv2

import game.states.CameraGameStateMain

ingevoerdeCode = []

# frame = game.states.CameraGameStateMain.frame

# ================================ Ik krijg het Frame niet nullable om in te zetten los van de class


def optellenVingersCodeCv():
    cv2.putText(frame, "Goed", (270, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
    cv2.rectangle(frame, pt1=(150, 150), pt2=(100, 100), color=(0, 255, 0), thickness=-1)
    cv2.putText(frame, "Geheime code:  " + str(ingevoerdeCode), (70, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0),
                2)


def geheimeCodeCv():
    cv2.putText(frame, "Geheime code:  " + str(ingevoerdeCode), (70, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                (0, 255, 0),
                2)


def displayFrameCv():
    cv2.imshow('VingerTellerCode', frame)


def nietGoed():
    cv2.putText(frame, "Niet Goed", (270, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
