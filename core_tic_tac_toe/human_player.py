class HumanPlayer:

    def __init__(self, name, symbol, board, display):
        self.name = name
        self.symbol = symbol
        self.board = board
        self.display = display

    def get_name(self):
        return self.name

    def get_symbol(self):
        return self.symbol

    def get_board(self):
        return self.board

    def make_move(self):
        player_input = int(self.display.get_player_input()) - 1

        if self.board.valid_move(player_input):
            self.board.execute_move(player_input, self.get_symbol())
        else:
            self.display.print_invalid_move_message()
            self.make_move()
