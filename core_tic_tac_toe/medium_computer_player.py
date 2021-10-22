class MediumComputerPlayer:

    def __init__(self, name, symbol, board, opponent_symbol):
        self.__name = name
        self.__symbol = symbol
        self.__board = board
        self.__opponent_symbol = opponent_symbol

    @property
    def symbol(self):
        return self.__symbol

    @property
    def board(self):
        return self.__board

    @property
    def name(self):
        return self.__name

    @property
    def game_logic(self):
        return self.__game_logic

    @property
    def opponent_symbol(self):
        return self.__opponent_symbol

    def make_move(self):
        horizontals_verticals_diagonals = self.board.get_all_positions()
        available_positions = self.board.get_available_positions()

        move_to_win_or_block = self.__move_to_win_or_block(
            horizontals_verticals_diagonals, available_positions)

        computer_move = self.__get_computer_move(
            move_to_win_or_block, available_positions)

        self.board.execute_move(computer_move - 1, self.symbol)

    def check_for_win(self, all_combinations, symbol, available_positions):
        for combination in all_combinations:
            for idx, value in enumerate(combination):
                if value in available_positions:
                    combination[idx] = symbol
                    if self.is_one_move_from_winning(combination, symbol):
                        return value
                    else:
                        combination[idx] = value

        return None

    def is_one_move_from_winning(self, combination, symbol):
        for value in combination:
            if value != symbol:
                return False

        return True

    def __get_computer_move(self, move_to_win_or_block, available_positions):
        if move_to_win_or_block:
            return move_to_win_or_block
        else:
            return available_positions.pop(0)

    def __move_to_win_or_block(self, horizontals_verticals_diagonals, available_positions):
        move_to_win = self.check_for_win(
            horizontals_verticals_diagonals, self.symbol, available_positions)

        if move_to_win:
            return move_to_win

        move_to_block = self.check_for_win(
            horizontals_verticals_diagonals, self.opponent_symbol, available_positions)

        if move_to_block:
            return move_to_block
