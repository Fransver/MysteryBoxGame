import cv2 as cv
import matplotlib.pyplot as plt
import mediapipe as mp

from game.layer.visualisation.Hands import handen

# ================================
# Handen creëren
mp_hands = mp.solutions.hands  # visualisation koppelen
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5)  # de 2 handen
mp_drawing = mp.solutions.drawing_utils  # tekenen om de handen

# ================================
# Plaatje eigenschappen

image_1 = cv.imread('../andereSpellen/images/sampleHandtracking/GettyImages-CMI_025web-570d0cde3df78c7d9e329e38.jpg')
image_2 = cv.imread('../andereSpellen/images/sampleHandtracking/benefitsofplayingpianoarticleimage.jpg')
image_3 = cv.imread('../andereSpellen/images/sampleHandtracking/asl.jpg')

static_image_list = []
static_image_list.append(image_1)
static_image_list.append(image_2)
static_image_list.append(image_3)

image = static_image_list[1]


# Grootte van figuur bepalen.
plt.figure(figsize=[10, 10])
plt.title("Sample Image", fontsize=40)
plt.axis('off')
plt.imshow(image[:, :, ::-1])
plt.show()

# ================================
results = hands.process(cv.cvtColor(image, cv.COLOR_BGR2RGB))
image_height, image_width, _ = image.shape

# Hier maak ik een kopie van de input om de marks op te tekenen.
img_copy = image.copy()

# Kijken of de marks gevonden worden.
if results.multi_hand_landmarks:

    # De gevonden marks in een lijst stoppen.
    for hand_no, hand_landmarks in enumerate(results.multi_hand_landmarks):
        # Draw the hand landmarks on the copy of the sample image.
        mp_drawing.draw_landmarks(image=img_copy, landmark_list=hand_landmarks,
                                  connections=mp_hands.HAND_CONNECTIONS)


    fig = plt.figure(figsize=[20, 20])
    plt.title("Resultant Image", fontsize=40)
    plt.axis('off')
    plt.imshow(img_copy[:, :, ::-1])
    plt.show()


