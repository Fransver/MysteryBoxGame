import unittest


class TestTimer(unittest.TestCase):

    def test_timer_almost_runs_out(self):
        stressful_tune = False
        timer = 10
        if timer == 10:
            stressful_tune = True
            return stressful_tune

        self.assertTrue(stressful_tune, msg="Tune is playing")
        self.assertEqual(timer, 10)
