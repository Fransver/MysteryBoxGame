import unittest


class TestButtonSounds(unittest.TestCase):

    def test_play_game_sound_code_input_button(self):
        pygame_short_sound = False
        v_press = True

        if v_press:
            pygame_short_sound = True
            return pygame_short_sound

        self.assertTrue(pygame_short_sound)

