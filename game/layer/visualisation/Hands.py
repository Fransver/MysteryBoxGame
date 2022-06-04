import mediapipe as mp

mp_hands = mp.solutions.hands


def handen():
    hands = mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5)
    return hands
