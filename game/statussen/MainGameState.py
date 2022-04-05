import game.commands.Codes
import game.layer.Hands
import game.commands.Messages

from game.layer.HandenDectector import detectHandsLandmarks
from game.layer.UpdateTextIngevoerdeCode import *

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
geheimeCodeStandaard = game.commands.Codes.geheimecodetest()
geheimeCodeRandom = game.commands.Codes.geheimecodesrandom()
lichtjesLijst = game.commands.Codes.lichtjeslijst()


# ================================ Intro Message

introMessage = game.commands.Messages.consoleMessageCameraGame()


# ================================ Handendetectie zonder game elementen

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
        if sum(count.values()) == geheimeCodeStandaard[0] and keyboard.is_pressed('v')  :

            cv2.putText(frame, "Goed", (270, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
            cv2.rectangle(frame, pt1=(150, 150), pt2=(100, 100), color=(0, 255, 0), thickness=-1)
            ingevoerdeCode.append(geheimeCodeStandaard[0])
            print("Test 1 keer code nummer " + str(
                geheimeCodeStandaard[0]))  # test met 1 keer uitvoeren van code met goede antwoord
            message = str(geheimeCodeStandaard[0])
            arduino.send_to_arduino(message)
            geheimeCodeStandaard.pop(0)  # Met pop haal ik de eerste index weer uit de lijst
            print(ingevoerdeCode)

            cv2.putText(frame, "Geheime code:  " + str(ingevoerdeCode), (70, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                        (0, 255, 0),
                        2)  # Code branden, maar hoe even laten staan

            if not geheimeCodeStandaard:
                key = cv2.waitKey(2000)
                cv2.putText(frame, "Einde spel", (270, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                print("Einde spel")
                break

        if sum(count.values()) != geheimeCodeStandaard[0] and keyboard.is_pressed('v'):
            cv2.putText(frame, "Niet Goed", (270, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)






    # ================================
    cv2.putText(frame, "Geheime code:  " + str(ingevoerdeCode), (70, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                (0, 255, 0),
                2)  # Code branden, maar hoe even laten staan



    # Display the frame.
    cv2.imshow('VingerTellerCode', frame)

    k = cv2.waitKey(1)


    # ================================ EXIT

    # ESCAPE is afsluiten programma
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

