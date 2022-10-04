import unittest
from main import TicTacGame


class TestTicTacGame(unittest.TestCase):

    def setUp(self):
        self.tictacgame = TicTacGame()

    def test_not_number_input(self):
        # Пользователь ввёл не число
        self.assertEqual(self.tictacgame.validate_input('a'), False)
        self.assertEqual(self.tictacgame.validate_input(''), False)

    def test_incorrect_number_input(self):
        # Пользователь ввёл некорректно число (<1 или >9)
        self.assertEqual(self.tictacgame.validate_input(10), False)
        self.assertEqual(self.tictacgame.validate_input(0), False)

    def test_repeat_number_input(self):
        # Пользователь указал номер занятой клетки
        self.tictacgame.board[0] = 'X'
        self.assertEqual(self.tictacgame.validate_input(1), False)

    def test_check_winner(self):
        # Проверка функции определения победителя
        self.tictacgame.position_of_X = {1, 2, 3, 6}
        self.assertEqual(self.tictacgame.check_winner('X'), True)


if __name__ == "__main__":
    unittest.main()
