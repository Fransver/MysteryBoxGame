import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands  #scanner van de handen
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils # teken module
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #langzaam openen opgelost door cap dshow


while True:
   ret , img = cap.read()
   h, w, c = img.shape
   results = hands.process(img)

   if results.multi_hand_landmarks:
      for hand_landmark in results.multi_hand_landmarks:

          for id, lm in enumerate(hand_landmark.landmark):
              x , y = int(lm.x*w), int(lm.y*h)
              print(id, ":", x, y ) #geeft nu positie breedte en hoogte landmark in int ipv float
              if id == 8: # correspondeert met de landmarks uit het png plaatje (27 per hand)
                  cv2.circle(img, (x,y), 15, (255,0,0), cv2.FILLED) # hiermee teken ik een dikkere cirkel om een specifiek punt

              mp_draw.draw_landmarks(img, hand_landmark, mp_hands.HAND_CONNECTIONS,
                                mp_draw.DrawingSpec((1, 190, 200), 2,2),
                                mp_draw.DrawingSpec((153, 51, 255), 2,2)  # drawing specs via Tulp kleuren controle
                                )

   cv2.imshow("Hand Tracking", img)
   cv2.waitKey(1)
