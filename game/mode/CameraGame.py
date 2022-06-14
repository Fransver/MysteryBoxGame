import cv2
import game.layer.visualisation.Hands
import keyboard
import random
import game.commands

from game.commands.SpelActies import *
from game.layer.visualisation.HandenDectector import detectHandsLandmarks
from game.layer.visualisation.cvActie import *
from game.layer.visualisation.CountFingers import countFingers
from game.mysteryBox.SerialArduinoMocked import SerialArduinoMocked
from game.commands.Codes import *
from game.commands.Messages import *
from game.commands.Score import *

# ================================ Arduino Creëren
arduino = SerialArduinoMocked()

# ================================ # Camera instellen
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # langzaam openen opgelost door cap dshow

# ================================ HANDS
hands = game.layer.visualisation.Hands.handen()

# ================================ Code
ingevoerdeCode = []
optiesRandomCode = [0, 1, 2, 3, 4, 5, 6, 7, 8]
geheimeCodeRandom = GeheimeCode(random.sample(optiesRandomCode, 4))
geheimeCodeStandaard = GeheimeCode([4, 8, 3, 1])

# ================================ Intro Message

introMessage = console_message_explain()

# ================================ Score

score = Score()


# ================================ Window

class CameraGame:
    def __init__(self):
        self.score = score.score
        self.game = camera_game_level_1


# ================================ CameraGame functie
def camera_game_level_1(timer):
    prev = time.time()
    TIMER = timer  # <------ Timer secondes aanpassen

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

        # ================================ Timer Text
        font_cv = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, str(TIMER), (100, 450), font_cv, 2, (0, 255, 255), 4, cv2.LINE_AA)

        # ================================ De classes met Handendetector en CountFingers

        frame, results = detectHandsLandmarks(frame, hands, display=False)

        # Controleren of de marks zijn ontdekt.
        if results.multi_hand_landmarks:
            frame, fingers_statuses, count = countFingers(frame, results, display=False)

            # ================================ En interactie met het spel

            if sum(count.values()) == geheimeCodeStandaard.code[0] and keyboard.is_pressed('v'):
                count_action(geheimeCodeStandaard, ingevoerdeCode)

            if len(ingevoerdeCode) == 4:  # Probleem index out of range opgelost met len ipv range(len)
                score.update_score_win()
                # melodietje Arduino ??
                print("Succes!!")
                print("score is " + str(score.score))
                break

            elif sum(count.values()) != geheimeCodeStandaard.code[0] and keyboard.is_pressed('v'):
                nietGoed(frame)

        # ================================
        geheimeCodeCv(frame, ingevoerdeCode)
        if len(ingevoerdeCode) < 4 and TIMER == 0:
            end_game()
            break

        if len(ingevoerdeCode) < 4 and TIMER < 4:
            almost_time(frame)

        # Display het frame.
        displayFrame(frame)
        k = cv2.waitKey(1)

        # ESCAPE is afsluiten programma
        if k == 27:
            ingevoerdeCode.clear()
            break

    # cap.release()  # dit blockt het opnieuw openen van de webcam
    cv2.destroyAllWindows()


if __name__ == '__main__':
    game = CameraGame()
    game.game(timer=90)
    quit()
