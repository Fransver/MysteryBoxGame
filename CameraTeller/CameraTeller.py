import cv2

from TextBox import InvoerCodeConsole
from HandenDectector import detectHandsLandmarks
from CountFingers import countFingers
from CountFingers import mp_hands
from arduino.SerialArduinoMocked import SerialArduinoMocked

#================================ Arduino Creëren

arduino = SerialArduinoMocked()

#================================ # Camera instellen

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #langzaam openen opgelost door cap dshow
#================================ HANDS

hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5)

# # Static image mode staat op True zodat hij de input als IMAGE behandeld.
# # Dit is ideaal voor het behandelen van VIDEO-FRAMES (voor bijvoorbeeld gebarentaal etc.)
# # Voor het actief tracken moet ik deze dus op FALSE zetten.
# # Min detection confidence op 0.5 is dat alle trackings die minder betrouwbaar als 50% zijn worden genegeerd.


#Timer creëren
timer = int(20)

#================================ CODES

gegevenCode = [3,2,6,1]   #index geven door direct na lijst aan te geven
ingevoerdeCode = []

lichtjeEen = "#52, lichtje 1 aan"
lichtjeTwee = "#53, lichtje 2 aan"
lichtjeDrie = "#54, lichtje 3 aan"
lichtjeVier = "#55, lichtje 4 aan"
lichtjesLijst = [lichtjeEen, lichtjeTwee, lichtjeDrie, lichtjeVier]
#================================


while cap.isOpened():# connectie met camera


    ok, frame = cap.read()
    if not ok:
        continue

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
                cv2.putText(frame, "1e", (270, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                ingevoerdeCode.append(gegevenCode[0])
                print("Test 1 keer code nummer 1") # test met 1 keer uitvoeren van code na goede antwoord
                gegevenCode.pop(0) # Met pop haal ik de eerste index weer uit de lijst
                print(ingevoerdeCode)


        else:
                cv2.putText(frame, "Niet Goed", (270, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)




# ================================

    # Display the frame.
    cv2.imshow('VingerTellerCode', frame)




    k = cv2.waitKey(1)

    # ESCAPE is afsluiten programma
    if (k == 27):
        break

cap.release()
cv2.destroyAllWindows()


