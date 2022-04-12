import cv2


from game.layer.HandenDectector import detectHandsLandmarks
from game.layer.CountFingers import countFingers
from game.layer.CountFingers import mp_hands
from arduino.SerialArduinoMocked import SerialArduinoMocked

#Aanvulling na sprintdemo
#================================ Arduino Creëren

arduino = SerialArduinoMocked()

#================================ # Camera instellen

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #langzaam openen opgelost door cap dshow
#================================ HANDS


# # Static image mode staat op True zodat hij de input als IMAGE behandeld.
# # Dit is ideaal voor het behandelen van VIDEO-FRAMES (voor bijvoorbeeld gebarentaal etc.)
# # Voor het actief tracken moet ik deze dus op FALSE zetten.
# # Min detection confidence op 0.5 is dat alle trackings die minder betrouwbaar als 50% zijn worden genegeerd.


#Timer creëren
timer = int(20)


#=============================== CODES

gegevenCode = [3,2,6,1]   #index geven door direct na lijst aan te geven
ingevoerdeCode = []

#================================


while cap.isOpened():# connectie met camera


    ok, frame = cap.read()
    if not ok:
        continue

    hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5)

    # Selfie view door horizontale flip
    frame = cv2.flip(frame, 1)

    # Landmark detectie op het frame
    frame, results = detectHandsLandmarks(frame, hands, display=False)



    # Controleren of de marks zijn ontdekt.
    if results.multi_hand_landmarks:
        # Tel vinger in het frame
        frame, fingers_statuses, count = countFingers(frame, results, display=False)

        

        # Opmaak camerateller uit de code van de vingerteller halen
        if (sum(count.values()) == gegevenCode[0]):

                cv2.putText(frame, "Goed", (270, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                cv2.rectangle(frame, pt1=(150, 150), pt2=(100, 100), color=(0, 255, 0), thickness=-1)

                ingevoerdeCode.append(gegevenCode[0])
                print("Test 1 keer code nummer " + str(gegevenCode[0])) # test met 1 keer uitvoeren van code met goede antwoord
                message = str(gegevenCode[0])
                arduino.send_to_arduino(message)
                gegevenCode.pop(0) # Met pop haal ik de eerste index weer uit de lijst
                print(ingevoerdeCode)




                if not gegevenCode:
                    cv2.putText(frame, "Einde spel", (270, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    print("Einde spel")
                    key = cv2.waitKey(2000)
                    break


        else:
                cv2.putText(frame, "Niet Goed", (270, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)



    # ================================
    cv2.putText(frame, "Geheime code:  " + str(ingevoerdeCode), (70, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0),
                2)

    # Display the frame.
    cv2.imshow('VingerTellerCode', frame)




    k = cv2.waitKey(1)

    # ESCAPE is afsluiten programma
    if (k == 27):
        break

cap.release()
cv2.destroyAllWindows()


