import cv2
import matplotlib.pyplot as plt
import mediapipe as mp

# ================================
# Handen creëren
mp_hands = mp.solutions.hands  # mediapipe koppelen
hands = mp_hands.Hands
mp_drawing = mp.solutions.drawing_utils


# ================================

def detectHandsLandmarks(image, hands, draw=True, display=True):
    # De functie om landmarks te detecteren.
    # image = input
    # hands de gespotte handen om de actie op te zetten.
    # draw = een boolean om landmarks te tekenen als er handen worden gevonden
    # display = een boolean als de originele input en output met marks weergeven wordt.
    # returns: een kopie van de input met de marks erop getekend & print van de daadwerkelijk marks.

    # Kopie van input creëren
    output_image = image

    # Converteren naar een formaat dat opencv het kan lezen (BGR naar RGB)
    imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # De landmarks detectie over het plaatje heen zetten.
    results = hands.process(imgRGB)

    # Controleren of er landmarks gevonden zijn en tekenen als dit zo is.
    if results.multi_hand_landmarks and draw:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image=output_image, landmark_list=hand_landmarks,
                                      connections=mp_hands.HAND_CONNECTIONS,
                                      landmark_drawing_spec=mp_drawing.DrawingSpec(color=(255, 255, 255),
                                                                                   thickness=2, circle_radius=2),
                                      connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0),
                                                                                     thickness=2, circle_radius=2))

    if display:
        # Display origineel en output plaatje
        plt.figure(figsize=[15, 15])
        plt.subplot(121)
        plt.imshow(image[:, :, ::-1])
        plt.title("Original Image", fontsize=40)
        plt.show()
        plt.axis('off')

        plt.subplot(122)
        plt.imshow(output_image[:, :, ::-1])  # imshow / matplot en tkinter Matplot vervangen door Tkinter.
        plt.title("Output", fontsize=40)
        plt.axis('off')
        plt.show()


    else:
        # Return output met de marks erop.
        return output_image, results
