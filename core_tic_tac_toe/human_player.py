class HumanPlayer:

    def __init__(self, name, symbol, board, io):
        self.name = name
        self.symbol = symbol
        self.board = board
        self.io = io

    def get_name(self):
        return self.name

    def get_symbol(self):
        return self.symbol

    def get_board(self):
        return self.board

    def make_move(self):
        player_input = int(self.io.get_player_input()) - 1

        if self.board.valid_move(player_input):
            self.board.execute_move(player_input, self.get_symbol())
        else:
            self.io.print_message("Invalid position, please try again!")
            self.make_move()
