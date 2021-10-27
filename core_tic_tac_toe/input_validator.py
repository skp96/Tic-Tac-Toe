import string


class InputValidator:

    def is_move_valid(self, input_move, board):
        if not self.__contains_invalid_character(input_move) and input_move.isdigit():
            player_input = int(input_move) - 1
            return board.valid_move(player_input)
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

    def __contains_invalid_character(self, input_move):
        return self.__is_alpha(input_move) or self.__is_white_space(input_move) or self.__is_special_character(input_move) or self.__contains_space(input_move) or self.__is_empty_space(input_move)

    def __is_alpha(self, input_move):
        return input_move.isalpha()

    def __is_white_space(self, input_move):
        return input_move.isspace()

    def __is_special_character(self, input_move):
        return input_move in string.punctuation

    def __contains_space(self, input_move):
        return " " in input_move

    def __is_empty_space(self, input_move):
        return input_move == ""
