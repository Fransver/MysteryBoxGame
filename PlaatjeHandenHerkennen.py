import cv2

from CameraTeller.HandenDectector import detectHandsLandmarks
from CameraTeller.HandenDectector import hands

image = cv2.imread('images/benefitsofplayingpianoarticleimage.jpg')
detectHandsLandmarks(image, hands, display=True )