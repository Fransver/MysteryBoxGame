import cv2

from game.layer.visualisation.HandenDectector import detectHandsLandmarks
from game.layer.visualisation.HandenDectector import hands

image = cv2.imread('images/sampleHandtracking/benefitsofplayingpianoarticleimage.jpg')
detectHandsLandmarks(image, hands, display=True )