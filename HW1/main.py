
class TicTacGame:
    board = list(range(1, 10))
    position_of_X = set()
    position_of_O = set()

    def show_board(self):
        # Отображение игрового поля
        for i in range(0, 7, 3):
            print(' ——— ——— ——— ')
            print("|", self.board[i], "|", self.board[i + 1], "|",
                  self.board[i + 2], "|")
        print(' ——— ——— ——— ')

    def validate_input(self, answer_player):
        # Валидация пользовательского ввода
        valid = True
        try:
            answer_player = int(answer_player)
        except ValueError:
            print("Введено не число")
            valid = False
        else:
            if (answer_player < 1 or answer_player > 9):
                print("Такого номера клетки не существует")
                valid = False
            elif (str(self.board[answer_player-1]) in {'X', 'O'}):
                print("Эта клетка уже занята")
                valid = False
        return valid

    def take_input(self, player):
        # Пользовательский ввод
        answer_player = input("Игрок " + player + ", Ваш ход:")
        if ((self.validate_input(answer_player)) is True):
            self.board[int(answer_player)-1] = player
            if player == 'X':
                self.position_of_X.add(int(answer_player))
            else:
                self.position_of_O.add(int(answer_player))
            self.show_board()
        else:
            return False

    def start_game(self):
        # Процесс игры
        print("Старт игры")
        self.show_board()
        win = False
        while not win:
            while ((self.take_input('X')) is False):
                continue
            if (self.check_winner('X')):
                win = True
                break
            # Проверка на ничью
            Nobody_win = True
            for each in self.board:
                if each in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
                    Nobody_win = False
                    break
            if (Nobody_win is True):
                print("Ничья!")
                win = True
                break
            while ((self.take_input('O')) is False):
                continue
            if (self.check_winner('O')):
                win = True
        print("Конец игры!")

    def check_winner(self, player):
        # Проверка на то, что есть ли победитель
        win_sets = ({1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7},
                    {3, 6, 9}, {2, 5, 8}, {1, 5, 9}, {3, 5, 7})
        if player == 'X':
            set_of_positions = self.position_of_X
        else:
            set_of_positions = self.position_of_O
        for each_win_set in win_sets:
            if each_win_set.difference(set_of_positions) == set():
                print('Победитель: ' + player)
                return True
        return False


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
