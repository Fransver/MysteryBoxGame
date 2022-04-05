import cv2

from game.layer.HandenDectector import detectHandsLandmarks
from game.layer.HandenDectector import hands

image = cv2.imread('../images/sampleHandtracking/benefitsofplayingpianoarticleimage.jpg')
detectHandsLandmarks(image, hands, display=True )