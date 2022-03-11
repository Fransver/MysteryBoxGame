import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands  #scanner van de handen
hands = mp_hands.Hands()
fingerTips = [8, 12, 16, 20]
thumbTips = 4
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
           for id, lm in enumerate(hand_landmark.landmark):
               lm_list.append(lm)
           finger_fold_status = []
           for tip in fingerTips:
               x, y = int(lm_list[tip].x * w), int(lm_list[tip].y * h) #alle vingertoppen uit de lijst x maal breedte, y maal hoogte
               # print(id, ":", x, y) #geeft nu positie breedte en hoogte landmark in int ipv float
               cv2.circle(img, (x, y), 15, (255, 0, 0), cv2.FILLED) # hiermee teken ik een dikkere cirkel om een specifiek punt

               mp_draw.draw_landmarks(img, hand_landmark, mp_hands.HAND_CONNECTIONS,
                          mp_draw.DrawingSpec((1, 190, 200), 2, 2),
                          mp_draw.DrawingSpec((153, 51, 255), 2, 2)  # drawing specs via Tulp kleuren controle
                          )

   cv2.imshow("Hand Tracking", img)
   cv2.waitKey(1)






