import unittest
import cv2
import mediapipe as mp

from game.layer.visualisation.HandenDectector import detectHandsLandmarks

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5)  # de 2 handen

image_1 = cv2.imread('../andereSpellen/images/sampleHandtracking/landmark.png')
image_2 = cv2.imread('../andereSpellen/images/sampleHandtracking/benefitsofplayingpianoarticleimage.jpg')
image_3 = cv2.imread('../andereSpellen/images/sampleHandtracking/asl.jpg')


class Test(unittest.TestCase):
    def test_static_detector_if_it_reads_hands_jpg(self):

        if detectHandsLandmarks(image_2, hands, draw=True, display=False):
            detection = True
            self.assertTrue(detection)

    def test_static_detector_if_it_read_hands_png(self):

        if detectHandsLandmarks(image_1, hands, draw=True, display=False):
            detection = True
            self.assertTrue(detection)
