class Display:

    def __init__(self, io):
        self.io = io

    def print_board(self, moves):
        horizontal_bar = self.__horizontal_bar()
        vertical_bars = self.__vertical_bars()

        board = (
            vertical_bars +
            "  {}  |  {}  |  {} \n".format(moves[0], moves[1], moves[2]) +
            vertical_bars +
            horizontal_bar +
            vertical_bars +
            "  {}  |  {}  |  {} \n".format(moves[3], moves[4], moves[5]) +
            vertical_bars +
            horizontal_bar +
            vertical_bars +
            "  {}  |  {}  |  {} \n".format(moves[6], moves[7], moves[8]) +
            vertical_bars
        )

        self.io.print_message(board)

    def print_invalid_move_message(self):
        self.io.print_message("Invalid position, please try again!")

    def get_player_input(self):
        return self.io.get_player_input()

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

    def __horizontal_bar(self):
        return "-----------------\n"

    def __vertical_bars(self):
        return "     |     |    \n"
