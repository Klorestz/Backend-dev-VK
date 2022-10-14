"""В модуле реализовано тестирование игры в крестики-нолики."""
import unittest
from unittest import mock
from unittest.mock import patch
import io
from main import TicTacGame
class TestTicTacGame(unittest.TestCase):
    """Класс для тестирования игры крестики-нолики."""
    def setUp(self):
        self.tictacgame = TicTacGame()

    @patch('builtins.print')
    def test_not_number_input(self, mock_print):
        """Пользователь ввёл не число."""
        TicTacGame.validate_input(self, 'a')
        mock_print.assert_called_with("Введено не число")

    def test_incorrect_number_input(self):
        """Пользователь ввёл некорректно число (<1 или >9)."""
        with mock.patch('sys.stdout', new=io.StringIO()):
            self.assertEqual(self.tictacgame.validate_input(10), False)
            self.assertEqual(self.tictacgame.validate_input(0), False)

    def test_repeat_number_input(self):
        """Пользователь указал номер занятой клетки."""
        with mock.patch('sys.stdout', new=io.StringIO()):
            self.tictacgame.board[0] = 'X'
            self.assertEqual(self.tictacgame.validate_input(1), False)

    def test_check_winner(self):
        """Проверка функции определения победителя."""
        with mock.patch('sys.stdout', new=io.StringIO()):
            self.tictacgame.position_of_X = {1, 2, 3, 6}
            self.assertEqual(self.tictacgame.check_winner('X'), True)


if __name__ == "__main__":
    unittest.main()
