import random
import game.layer.Hands
import keyboard

from game.commands.SpelActies import *
from game.layer.opencv.cvActie import *
from game.layer.CountFingers import countFingers
from game.mysteryBox.arduino.SerialArduinoMocked import SerialArduinoMocked
from game.commands.Codes import *
from game.commands.Messages import *
from game.states.FailScreen import *


# ================================ Arduino Creëren
arduino = SerialArduinoMocked()

# ================================ # Camera instellen
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # langzaam openen opgelost door cap dshow

# ================================ HANDS
hands = game.layer.Hands.handen()

# ================================ Code
ingevoerdeCode = []
optiesRandomCode = [0, 1, 2, 3, 4, 5, 6, 7, 8]
geheimeCodeRandom = geheimeCode("random", random.sample(optiesRandomCode, 4))
geheimeCodeStandaard = geheimeCode("standaard", [1, 2, 3, 4])

# ================================ Intro Message

introMessage = consoleMessageCameraGame()


# ================================ Handendetectie zonder game elementen
def CameraGame():
    prev = time.time()
    TIMER = int(40)

    while cap.isOpened():  # connectie met camera

        # ================================ Timer Functie
        cur = time.time()
        if cur - prev >= 1:
            prev = cur
            TIMER = TIMER - 1

        ok, frame = cap.read()
        if not ok:
            continue
        # Selfie view door horizontale flip
        frame = cv2.flip(frame, 1)

        ## ================================ Timer Text
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, str(TIMER), (100, 450), font, 2, (0, 255, 255), 4, cv2.LINE_AA)

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
                break

            if sum(count.values()) != geheimeCodeStandaard.code[0] and keyboard.is_pressed('v'):
                nietGoed(frame)

        # ================================
        geheimeCodeCv(frame, ingevoerdeCode)

        if TIMER <= 0:
            cap.release()
            cv2.destroyAllWindows()
            window_fail()


        # Display het frame.
        displayFrame(frame)
        k = cv2.waitKey(1)

        # ESCAPE is afsluiten programma
        if k == 27:
            break
    # ================================ EXIT

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    CameraGame()
