import unittest


count = {'RIGHT': 0, 'LEFT': 0}


class TestMockFingersCount(unittest.TestCase):

    def test_count_of_fingers_mock_output(self):
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
