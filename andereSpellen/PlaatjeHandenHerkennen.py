import cv2

from game.layer.mediapipe.HandenDectector import detectHandsLandmarks
from game.layer.mediapipe.HandenDectector import hands

image = cv2.imread('images/sampleHandtracking/benefitsofplayingpianoarticleimage.jpg')
detectHandsLandmarks(image, hands, display=True )