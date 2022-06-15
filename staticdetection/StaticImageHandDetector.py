import cv2
import mediapipe
import matplotlib.pyplot as plt

from game.layer.visualisation.HandenDectector import *
from game.layer.visualisation.Hands import *


def static_detector():
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5)  # de 2 handen

    image_1 = cv2.imread('../andereSpellen/images/sampleHandtracking/GettyImages-CMI_025web-570d0cde3df78c7d9e329e38.jpg')
    image_2 = cv2.imread('../andereSpellen/images/sampleHandtracking/benefitsofplayingpianoarticleimage.jpg')
    image_3 = cv2.imread('../andereSpellen/images/sampleHandtracking/asl.jpg')

    static_image_list = [image_1, image_2, image_3]
    image = static_image_list[1]

    # Grootte van figuur bepalen.
    plt.figure(figsize=[10, 10])
    plt.title("Sample Image", fontsize=40)
    plt.axis('off')
    plt.imshow(image[:, :, ::-1])
    plt.show()

    detectHandsLandmarks(image, hands, draw=True, display=True)


if __name__ == '__main__':
    static_detector()
