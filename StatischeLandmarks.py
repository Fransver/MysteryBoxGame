import cv2 as cv
import matplotlib.pyplot as plt
import mediapipe as mp

#================================

# Handen creëren
mp_hands = mp.solutions.hands # mediapipe koppelen

hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5) # de 2 handen
# Static image mode staat op True zodat hij de input als IMAGE behandeld.
# Dit is ideaal voor het behandelen van VIDEO-FRAMES (voor bijvoorbeeld gebarentaal etc.)
# Voor het actief tracken moet ik deze dus op FALSE zetten.
# Min detection confidence op 0.5 is dat alle trackings die minder betrouwbaar als 50% zijn worden genegeerd.

mp_drawing = mp.solutions.drawing_utils # tekenen om de handen

#================================
# Plaatje eigenschappen
image = cv.imread('telplaatjes/hand1.jpg')
# Grootte van figuur bepalen.
plt.figure(figsize=[10, 10])
plt.title("Sample Image", fontsize = 40)
plt.axis('off')
plt.imshow(image[:, :, ::-1])
plt.show()

#================================

results = hands.process(cv.cvtColor(image, cv.COLOR_BGR2RGB)) # converteren van BGR naar RGB
# Plaatje omzetten naar specifieke schaal om preciezer de landmarks te tekenen.
# Plaatje converteren en detecteren
# Perform hands landmarks detection after converting the image into RGB format.

# Kijken of er landmarks gevonden zijn.
if results.multi_hand_landmarks:
    # Uitleg over de assen
    # X = de breedte
    # Y = de hoogte
    # Z = de diepte (gebaseerd op de pols en de camera)

    # De gevonden marks in een lijst stoppen..
    for hand_no, hand_landmarks in enumerate(results.multi_hand_landmarks):

        print(f'HAND NUMBER: {hand_no + 1}')
        print('-----------------------')

        # Iterate two times as we only want to display first two landmarks of each hand.
        for i in range(2):
            # Display the found normalized landmarks.
            print(f'{mp_hands.HandLandmark(i).name}:')
            print(f'{hand_landmarks.landmark[mp_hands.HandLandmark(i).value]}')

#================================

image_height, image_width, _ = image.shape

# Check if landmarks are found.
if results.multi_hand_landmarks:

    # Iterate over the found hands.
    for hand_no, hand_landmarks in enumerate(results.multi_hand_landmarks):

        print(f'HAND NUMBER: {hand_no + 1}')
        print('-----------------------')

        # Iterate two times as we only want to display first two landmark of each hand.
        for i in range(2):
            # Display the found landmarks after converting them into their original scale.
            # Terugbrengen naar originele grootte van de schaal
            # Retrieve the height and width of the sample image.
            print(f'{mp_hands.HandLandmark(i).name}:')
            print(f'x: {hand_landmarks.landmark[mp_hands.HandLandmark(i).value].x * image_width}')
            print(f'y: {hand_landmarks.landmark[mp_hands.HandLandmark(i).value].y * image_height}')
            print(f'z: {hand_landmarks.landmark[mp_hands.HandLandmark(i).value].z * image_width}\n')

#================================
# Hier maak ik een kopie van de input om de marks op te tekenen.
img_copy = image.copy()

# Kijken of de marks gevonden worden.
if results.multi_hand_landmarks:

    # De gevonden marks in een lijst stoppen.
    for hand_no, hand_landmarks in enumerate(results.multi_hand_landmarks):
        # Draw the hand landmarks on the copy of the sample image.
        mp_drawing.draw_landmarks(image=img_copy, landmark_list=hand_landmarks,
                                  connections=mp_hands.HAND_CONNECTIONS)

    # Specify a size of the figure.
    fig = plt.figure(figsize=[20, 20])

    # Display the resultant image with the landmarks drawn, also convert BGR to RGB for display.
    plt.title("Resultant Image", fontsize = 40);
    plt.axis('off');
    plt.imshow(img_copy[:, :, ::-1]);
    plt.show()

# ================================




