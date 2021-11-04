class Display:

    def __init__(self, io):
        self.io = io

    def print_board(self, moves):

        board = ""

        for idx, move in enumerate(moves):
            board += self.__generate_vertical_bars(move)
            board += self.__generate_rows(move)
            board += self.__generate_vertical_bars(move)

            if idx != len(moves) - 1:
                board += self.__generate_horizontal_bars(move)

        self.io.print_message(board)

    def print_invalid_move_message(self):
        self.io.print_message("Invalid position, please try again!")

    def get_player_input(self):
        user_move = self.io.get_player_input()
        return user_move

    def print_player_turn(self, player_name):
        self.io.print_message(f"{player_name} it's your turn!")

    def announce_winner(self, player_name):
        self.io.print_message(
            f"We have a winner, congratulations {player_name}")

    def announce_tie(self):
        self.io.print_message("Good game, but it's a tie!")

    def welcome_message(self):
        self.io.print_message("Welcome to Tic Tac Toe\n")

    def game_options(self, message):
        self.io.print_message(message)

    def clear_console(self):
        self.io.clear_console()

    def print_invalid_game_selection_message(self):
        self.io.print_message("Invalid option, please try again!")

    def __generate_horizontal_bars(self, move):
        return ("-----------" * len(move)) + "\n"

    def __generate_vertical_bars(self, move):
        vertical_bars = ""

        for idx in range(0, len(move)):
            if idx != len(move) - 1:
                vertical_bars += "          |"
            else:
                vertical_bars += "          \n"

        return vertical_bars

    def __generate_rows(self, move):
        row = ""

        for idx, position in enumerate(move):
            if idx != len(move) - 1:
                if type(position) == int and self.__is_double_digit(position):
                    row += "    {}    |".format(position)
                else:
                    row += "     {}    |".format(position)
            else:
                row += "     {}     \n".format(position)

        return row

    def __is_double_digit(self, value):
        return value // 10 > 0
