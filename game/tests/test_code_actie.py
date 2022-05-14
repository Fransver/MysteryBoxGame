import unittest
import random
from game.commands.Codes import *


class TestCodeAction(unittest.TestCase):

    def test_code_standaard_actie_append_from_given_code(self):  # eerste eenvoudige test
        given_code = [1, 2, 3, 4]
        input_code_list = [given_code[0]]

        given_code.pop(0)
        code_length_after_action = len(given_code)

        self.assertEqual(code_length_after_action, 3)

    def test_code_is_random_4_numbers(self):
        option_random_code = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        random_code = GeheimeCode(random.sample(option_random_code, 4))
        random_code_length = len(random_code.code)
        given_numbers = 4

        self.assertEqual(given_numbers, random_code_length)




if __name__ == '__main__':
    unittest.main()
