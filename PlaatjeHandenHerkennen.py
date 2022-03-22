import cv2
import matplotlib.pyplot as plt
import mediapipe as mp

from HandenDectector import detectHandsLandmarks
from HandenDectector import hands

image = cv2.imread('images/benefitsofplayingpianoarticleimage.jpg')
detectHandsLandmarks(image, hands, display=True )