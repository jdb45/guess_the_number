import guess_the_number
import unittest
from unittest.mock import patch
class TestRandGuess(unittest.TestCase):
    # @patch ('guess_the_number.configure_range', return_value = (1, 10))
    # @patch('builtins.input', side_effect=[3,6,4])
    # @patch ('random.randint', return_value=4)
    @patch ('builtins.print')
    # @patch ('guess_the_number.again', return_value = 'sys.exit()')
    # def test_randWinLose(self, mock_end, mock_print, mock_random, mock_input, mock_range):
    def test_randWinLose(self, mock_print):

        self.assertEqual('too low', guess_the_number.check_guess(3,4,3))

        self.assertEqual('too high', guess_the_number.check_guess(5,4,3))
        self.assertEqual('you guessed correctly after 3 tries!', guess_the_number.check_guess(4,4,3))
        # guess_the_number.check_guess(4,4,3)
        # mock_print.assert_called_with(guess_the_number.correct)
