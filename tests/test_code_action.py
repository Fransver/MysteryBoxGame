import unittest
import random

import game.commands.Codes
from game.commands.Codes import *


# Code false message
# Timer testen

given_code = game.commands.Codes.GeheimeCode([1, 4, 6, 2])
option_random_code = [0, 1, 2, 3, 4, 5, 6, 7, 8]
random_code = GeheimeCode(random.sample(option_random_code, 4))


class TestCodeAction(unittest.TestCase):

    def test_code_standaard_actie_append_from_given_code(self):
        given_code.code.pop(0)
        code_length_after_action = len(given_code.code)

        self.assertEqual(code_length_after_action, 3)

    def test_code_is_random_4_numbers(self):

        random_code_length = len(random_code.code)
        given_numbers = 4

        self.assertEqual(given_numbers, random_code_length)


if __name__ == '__main__':
    unittest.main()
