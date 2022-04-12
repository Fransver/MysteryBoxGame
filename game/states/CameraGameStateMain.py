import game.commands.Codes
import random
import game.layer.Hands
import game.commands.Messages
import time
import keyboard


from game.layer.HandenDectector import detectHandsLandmarks
from game.layer.cvActie import *
from game.layer.CountFingers import countFingers
from arduino.SerialArduinoMocked import SerialArduinoMocked

# ================================ Arduino Creëren
arduino = SerialArduinoMocked()

# ================================ # Camera instellen
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # langzaam openen opgelost door cap dshow

# ================================ HANDS
hands = game.layer.Hands.handen()

# ================================ Code
ingevoerdeCode = []
optiesRandomCode = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
geheimeCodeStandaard = game.commands.Codes.geheimeCode("TestCode1", [2,4,8,1])
geheimeCodeRandom = game.commands.Codes.geheimeCode("RandomCode1", random.sample(optiesRandomCode, 4))

# ================================ Intro Message

introMessage = game.commands.Messages.consoleMessageCameraGame()


# ================================ Handendetectie zonder game elementen
def CameraGame():
    while cap.isOpened():  # connectie met camera

        ok, frame = cap.read()
        if not ok:
            continue

        # Selfie view door horizontale flip
        frame = cv2.flip(frame, 1)

        # ================================ De classes met Handendetector en CountFingers
        # Landmark detectie op het frame
        frame, results = detectHandsLandmarks(frame, hands, display=False)

        # Controleren of de marks zijn ontdekt.
        if results.multi_hand_landmarks:
            # Tel vinger in het frame
            frame, fingers_statuses, count = countFingers(frame, results, display=False)

            # ================================ En interactie met het spel
            # Het is gelukt om de actie van toevoegen code pas op de knop V te doen
            if sum(count.values()) == geheimeCodeStandaard.code[0] and keyboard.is_pressed('v'):
                ingevoerdeCode.append(geheimeCodeStandaard.code[0])
                message = str(geheimeCodeStandaard.code[0])
                time.sleep(1)  # kort moment van input zodat er niet meteen achter elkaar gedrukt kan worden.
                arduino.send_to_arduino(message)
                print(ingevoerdeCode)
                geheimeCodeStandaard.code.pop(0)  # Met pop haal ik de eerste index weer uit de lijst

                if not geheimeCodeStandaard:
                    cv2.putText(frame, "Einde spel", (270, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    print("Einde spel")
                    time.sleep(5)
                    break

            if sum(count.values()) != geheimeCodeStandaard.code[0] and keyboard.is_pressed('v'):
                cv2.putText(frame, "Niet Goed", (270, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

        # ================================


        cv2.putText(frame, "Geheime code:  " + str(ingevoerdeCode), (70, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                    (0, 255, 0),
                    2)

        # Display the frame.
        cv2.imshow('VingerTellerCode', frame)
        k = cv2.waitKey(1)

        # ================================ EXIT

        # ESCAPE is afsluiten programma
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

    class visualCVACties:

        def geheimecodeCV(self):
            cv2.putText(frame, "Geheime code:  " + str(ingevoerdeCode), (70, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                        (0, 255, 0),
                        2)


