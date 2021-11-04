class GameLogic:

    def check_winner(self, board, symbol):
        for combination in board:
            if self.__check_combination_for_win(combination, symbol):
                return True

        return False

    def is_tie(self, board, symbol):
        return self.__is_board_full(board) and not self.check_winner(board, symbol)

    def __is_board_full(self, board):
        for combination in board:
            for value in combination:
                if type(value) == int:
                    return False

        return True

    def __check_combination_for_win(self, combination, symbol):
        for value in combination:
            if value != symbol:
                return False

        return True
