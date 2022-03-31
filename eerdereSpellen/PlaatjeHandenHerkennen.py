import cv2

from game.mysteryBox.HandenDectector import detectHandsLandmarks
from game.mysteryBox.HandenDectector import hands

image = cv2.imread('../images/benefitsofplayingpianoarticleimage.jpg')
detectHandsLandmarks(image, hands, display=True )