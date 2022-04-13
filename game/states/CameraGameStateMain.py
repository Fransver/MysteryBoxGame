import random
import game.layer.Hands
import time
import keyboard

from game.layer.HandenDectector import detectHandsLandmarks
from game.commands.SpelActies import *
from game.layer.cvActie import *
from game.layer.CountFingers import countFingers
from game.mysteryBox.arduino.SerialArduinoMocked import SerialArduinoMocked
from game.commands.Codes import *
from game.commands.Messages import *

# ================================ Arduino Creëren
arduino = SerialArduinoMocked()


# ================================ # Camera instellen
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # langzaam openen opgelost door cap dshow


# ================================ HANDS
hands = game.layer.Hands.handen()

# ================================ Code
ingevoerdeCode = []
optiesRandomCode = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
geheimeCodeRandom = geheimeCode("random", random.sample(optiesRandomCode, 4))
geheimeCodeStandaard = geheimeCode("standaard", [1, 2, 3, 4])

# ================================ Intro Message

introMessage = consoleMessageCameraGame()


# ================================ Handendetectie zonder game elementen
def CameraGame():
    while cap.isOpened():  # connectie met camera

        ok, frame = cap.read()
        if not ok:
            continue
        # Selfie view door horizontale flip
        frame = cv2.flip(frame, 1)

        # ================================ De classes met Handendetector en CountFingers

        frame, results = detectHandsLandmarks(frame, hands, display=False)
        # Controleren of de marks zijn ontdekt.
        if results.multi_hand_landmarks:
            frame, fingers_statuses, count = countFingers(frame, results, display=False)

            # ================================ En interactie met het spel
            if sum(count.values()) == geheimeCodeStandaard.code[0] and keyboard.is_pressed('v'):
                telActie(geheimeCodeStandaard, ingevoerdeCode)

            if len(ingevoerdeCode) == 4:  # lijst tot aantal nummers gevuld? Dan complete-actie !!
                eindeSpel(frame)
                print("Einde spel")
                time.sleep(5)
                break

            if sum(count.values()) != geheimeCodeStandaard.code[0] and keyboard.is_pressed('v'):
                nietGoed(frame)

        # ================================
        geheimeCodeCv(frame)

        # Display het frame.
        cv2.imshow('VingerTellerCode', frame)
        k = cv2.waitKey(1)

        # ================================ EXIT

        # ESCAPE is afsluiten programma
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

