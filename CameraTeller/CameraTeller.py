import cv2

#================================
# Handen & Functies creëren
from HandenDectector import detectHandsLandmarks
from CountFingers import countFingers
from CountFingers import mp_hands


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #langzaam openen opgelost door cap dshow

hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5)
# # Static image mode staat op True zodat hij de input als IMAGE behandeld.
# # Dit is ideaal voor het behandelen van VIDEO-FRAMES (voor bijvoorbeeld gebarentaal etc.)
# # Voor het actief tracken moet ik deze dus op FALSE zetten.
# # Min detection confidence op 0.5 is dat alle trackings die minder betrouwbaar als 50% zijn worden genegeerd.


#================================

#Timer creëren
timer = int(20)

#================================

# gegevenCode = [3,2,6,1]


#================================



while cap.isOpened(): # connectie met camera

    ok, frame = cap.read()
    if not ok:
        continue

    # Selfie view door horizontale flip
    frame = cv2.flip(frame, 1)

    # Landmark detectie op het frame
    frame, results = detectHandsLandmarks(frame, hands, display=False)

    # Controleren of de marks zijn ontdekt.
    if results.multi_hand_landmarks:
        # Tel het aantal vingers in het frame
        frame, fingers_statuses, count = countFingers(frame, results, display=False)








    # Display the frame.
    cv2.imshow('VingerTellerCode', frame)

    # Wait for 1ms. If a key is pressed, retreive the ASCII code of the key.
    k = cv2.waitKey(1)


    # ESCAPE is afsluiten programma
    if (k == 27):
        break
cap.release()
cv2.destroyAllWindows()

