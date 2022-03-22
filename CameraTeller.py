import cv2
import matplotlib.pyplot as plt
import mediapipe as mp
import time # Timer maken voor aftellen vingertelling

#================================
# Handen creëren
from HandenDectector import detectHandsLandmarks

mp_hands = mp.solutions.hands # mediapipe koppelen
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5) # de 2 handen
# Static image mode staat op True zodat hij de input als IMAGE behandeld.
# Dit is ideaal voor het behandelen van VIDEO-FRAMES (voor bijvoorbeeld gebarentaal etc.)
# Voor het actief tracken moet ik deze dus op FALSE zetten.
# Min detection confidence op 0.5 is dat alle trackings die minder betrouwbaar als 50% zijn worden genegeerd.
mp_drawing = mp.solutions.drawing_utils # tekenen om de handen

#================================

#Timer creëren
timer = int(20)

#================================



def countFingers(image, results, draw=True, display=True):

    # Breedte en Hoogte van de input
    height, width, _ = image.shape

    # Kopie maken om de vingers op te tekenen.
    output_image = image.copy()

    # Een dictionary bevat niet te dupliceren items. Ze kunnen overschreven worden door een duplicate.
    # Vorm lijkt een beetje op JSON.
    count = {'RIGHT': 0, 'LEFT': 0}

    # Wederom een dictionary voor de boolean waardes van beide handen.
    fingers_statuses = {'RIGHT_THUMB': False, 'RIGHT_INDEX': False, 'RIGHT_MIDDLE': False, 'RIGHT_RING': False,
                        'RIGHT_PINKY': False, 'LEFT_THUMB': False, 'LEFT_INDEX': False, 'LEFT_MIDDLE': False,
                        'LEFT_RING': False, 'LEFT_PINKY': False}

    # De vingertoppen in een array stoppen.
    fingers_tips = [mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
                        mp_hands.HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.PINKY_TIP]



    # Iterate over de gevonden handen
    for hand_index, hand_info in enumerate(results.multi_handedness):

        # Een label voor links of rechts toewijzen aan de gevonden handen.
        hand_label = hand_info.classification[0].label

        # De landmarks van de gevonden handen teruggeven.
        hand_landmarks = results.multi_hand_landmarks[hand_index]

        # Iterate over the indexes of the tips landmarks of each finger of the hand.
        for tip_index in fingers_tips:
            # Retrieve the label (i.e., index, middle, etc.) of the finger on which we are iterating upon.
            finger_name = tip_index.name.split("_")[0]

            # Dit is eigenlijk het belangrijkste van wat er gebeurt in het script
            # Ik gebruik hier de vingertoppen en als die boven het middenpunt komen verandert de status
            # Ook komt er dan een punt bij voor iedere opgestoken vinger
            if (hand_landmarks.landmark[tip_index].y <  hand_landmarks.landmark[tip_index - 2].y):
                fingers_statuses[hand_label.upper() + "_" + finger_name] = True

                # Increment the count of the fingers up of the hand by 1.
                count[hand_label.upper()] += 1

            # Retrieve the y-coordinates of the tip and mcp landmarks of the thumb of the hand.
            thumb_tip_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x
            thumb_mcp_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP - 2].x

            if (hand_label == 'Right' and (thumb_tip_x < thumb_mcp_x)) or (hand_label == 'Left' and (thumb_tip_x < thumb_mcp_x)):
                    # Update the status of the thumb in the dictionary to true.
                    fingers_statuses[hand_label.upper() + "_THUMB"] = True

                    # Increment the count of the fingers up of the hand by 1.
                    count[hand_label.upper()] += 1


    if draw:
        # Hier schrijf ik het totaal aantal vingers in de camera-feed
        cv2.putText(output_image, " Code invoer: ", (25, 25), cv2.FONT_HERSHEY_COMPLEX, 1, (205,51,51), 2)
        cv2.putText(output_image, str(sum(count.values())), (width // 2 - 150, 240), cv2.FONT_HERSHEY_SIMPLEX,
                    3, (220,20,60), 10, 10 ) #grootte, kleur, dikte cijfers

        # Hier ergens een if om de code te corresponderen ?
        if (sum(count.values()) == 2):
            cv2.putText(output_image, "Leuk", (270, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
        else:
            cv2.putText(output_image, "Niet leuk", (270, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)


    if display:
        # Display the output image.
        plt.figure(figsize=[10, 10])
        plt.imshow(output_image[:, :, ::-1])
        plt.title("Output Image")
        plt.axis('off')

    else:
        # Return the output image, the status of each finger and the count of the fingers up of both hands.
        return output_image, fingers_statuses, count


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #langzaam openen opgelost door cap dshow
while cap.isOpened(): # connectie met camera

    # Read a frame.
    ok, frame = cap.read()

    # Check if frame is not read properly then continue to the next iteration to read the next frame.
    if not ok:
        continue

    # Selfie view door horizontale flip
    frame = cv2.flip(frame, 1)

    # Perform Hands landmarks detection on the frame.
    frame, results = detectHandsLandmarks(frame, hands, display=False)

    # Check if the hands landmarks in the frame are detected.
    if results.multi_hand_landmarks:
        # Count the number of fingers up of each hand in the frame.
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