import cv2
import matplotlib.pyplot as plt
import mediapipe as mp
import Hands


#================================ Handen



hands = Hands.Hands
mp_hands = mp.solutions.hands
mp_drawing = Hands.DrawHands


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
            if (hand_landmarks.landmark[tip_index].y < hand_landmarks.landmark[tip_index - 2].y):
                fingers_statuses[hand_label.upper() + "_" + finger_name] = True

                # Increment the count of the fingers up of the hand by 1.
                count[hand_label.upper()] += 1

            # Retrieve the y-coordinates of the tip and mcp landmarks of the thumb of the hand.
            thumb_tip_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x
            thumb_mcp_x = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP - 2].x

            if (hand_label == 'Right' and (thumb_tip_x < thumb_mcp_x)) or (
                    hand_label == 'Left' and (thumb_tip_x < thumb_mcp_x)):
                # Update the status of the thumb in the dictionary to true.
                fingers_statuses[hand_label.upper() + "_THUMB"] = True

                # Increment the count of the fingers up of the hand by 1.
                count[hand_label.upper()] += 1

    if draw:

        # Hier schrijf ik het totaal aantal vingers in de camera-feed
        cv2.putText(output_image, " Code invoer: ", (25, 25), cv2.FONT_HERSHEY_COMPLEX, 1, (205, 51, 51), 2)
        cv2.putText(output_image, str(sum(count.values())), (width // 2 - 150, 240), cv2.FONT_HERSHEY_SIMPLEX,
                    3, (220, 20, 60), 10, 10)  # grootte, kleur, dikte cijfers



    if display:
        # Display the output image.
        plt.figure(figsize=[10, 10])
        plt.imshow(output_image[:, :, ::-1])
        plt.title("Output Image")
        plt.axis('off')

    else:
        # Return the output image, the status of each finger and the count of the fingers up of both hands.
        return output_image, fingers_statuses, count