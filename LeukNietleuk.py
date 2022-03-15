import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands  #scanner van de handen
hands = mp_hands.Hands()
fingerTips = [8, 12, 16, 20]
thumbTip = 4
finger_fold_status = []
mp_draw = mp.solutions.drawing_utils # teken module
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) #langzaam openen opgelost door cap dshow


while True:
   ret , img = cap.read()
   img = cv2.flip(img, 1)
   h, w, c = img.shape
   img.flags.writeable = False # prestatie verbeterd door niet als writable te markeren (begrijp het niet helemaal.)
   img =  cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
   results = hands.process(img)

   if results.multi_hand_landmarks:
       for hand_landmark in results.multi_hand_landmarks:
           lm_list = []
           for id, lm in enumerate(hand_landmark.landmark): #ennumarate voegt nummers toe aan een lijst van objecten
               lm_list.append(lm) #append is toevoegen van een item aan de lijst.
           finger_fold_status = []

           for tip in fingerTips:
               x, y = int(lm_list[tip].x * w), int(lm_list[tip].y * h) #alle vingertoppen uit de lijst x maal breedte, y maal hoogte
               # print(id, ":", x, y) #geeft nu positie breedte en hoogte landmark in int ipv float
               cv2.circle(img, (x, y), 10, (0, 255, 0), cv2.FILLED) # hiermee teken ik een dikkere cirkel om een specifiek punt

               if lm_list[tip].x < lm_list[tip - 3].x:
                   cv2.circle(img, (x, y), 15, (0, 0,255), cv2.FILLED)
                   finger_fold_status.append(True)
               else: finger_fold_status.append(False)

               mp_draw.draw_landmarks(img, hand_landmark, mp_hands.HAND_CONNECTIONS,
                          mp_draw.DrawingSpec((1, 190, 200), 2, 2),
                          mp_draw.DrawingSpec((153, 51, 255), 2, 2)  # draewing specs via Tulp kleuren controle
                          )

               print(finger_fold_status)

               if all(finger_fold_status):
                    # Leuk
                if lm_list[thumbTip].y < lm_list[thumbTip - 1].y < lm_list[thumbTip - 2].y:
                       print("Leuk")
                       cv2.putText(img, "Leuk", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

                            # Niet Leuk
                if lm_list[thumbTip].y > lm_list[thumbTip - 1].y > lm_list[thumbTip - 2].y:
                   cv2.putText(img, "Niet leuk", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                   print("Niet leuk")  # Hiermee print ik een niet leuk teken op het scherm


                if lm_list[fingerTips (0)].y < lm_list[fingerTips(0) -1].y:
                    cv2.putText(img, "test", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)



   cv2.imshow("Hand Tracking", img)
   cv2.waitKey(1)







