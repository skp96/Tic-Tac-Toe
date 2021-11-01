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
