import string


class InputValidator:

    def is_move_valid(self, input_move, board):
        if input_move.isdigit():
            return board.valid_move(input_move)
        else:
            return False

    def is_game_option_valid(self, game_option):
        if game_option.isdigit():
            option = int(game_option)
            return self.__check_range_of_options(option)
        else:
            return False

    def __check_range_of_options(self, game_option):
        return game_option >= 1 and game_option <= 4

    def is_board_size_valid(self, board_size):
        if board_size.isdigit():
            option = int(board_size)
            return self.__check_board_size_range(option)
        else:
            return False

    def __check_board_size_range(self, option):
        return option >= 3 and option < 10
