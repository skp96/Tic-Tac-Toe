class HumanPlayer:

    def __init__(self, name, symbol, board, display, input_validator):
        self.name = name
        self.symbol = symbol
        self.board = board
        self.display = display
        self.input_validator = input_validator

    def get_name(self):
        return self.name

    def get_symbol(self):
        return self.symbol

    def get_board(self):
        return self.board

    def make_move(self):
        input = self.display.get_player_input()

        if self.input_validator.is_move_valid(input, self.get_board()):
            player_input = int(input) - 1
            self.board.execute_move(player_input, self.get_symbol())
        else:
            self.display.print_invalid_move_message()
            self.make_move()
