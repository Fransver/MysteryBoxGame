import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #langzaam openen opgelost door cap dshow


while True:
   ret , img = cap.read()

   results = hands.process(img)
   print(results.multi_hand_landmarks)
   cv2.imshow("Live Feed", img)
   cv2.waitKey(1)

