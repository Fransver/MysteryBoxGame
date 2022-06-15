import unittest
from game.layer.visualisation.CountFingers import count_hands

count = count_hands()


# This unit test is created to precent breakage in Count dictonary within CountFingers Class

class TestMockFingersCount(unittest.TestCase):

    def test_count_of_fingers(self):
        game_code = [3, 2, 4, 1]  # game code for comparison
        count['RIGHT'] += 3  # incrementing Right hand 3 fingers
        result = sum(count.values())
        first_code = game_code[0]

        self.assertEqual(result, first_code)  # comparing first int code with finger output
        self.assertTrue(result == first_code)

    def test_message_count_fingers_not_correct(self):
        cv_message_incorrect = False
        game_code = [3, 2, 4, 1]  # game code for comparison
        count['RIGHT'] += 5  # incrementing Right hand 5 fingers
        result = sum(count.values())
        first_code = game_code[0]

        if result != first_code:
            cv_message_incorrect = True
            return cv_message_incorrect

        self.assertTrue(cv_message_incorrect, True)
        self.assertEqual(game_code[0], 3)
        self.assertEqual(result, 5)
