class HumanPlayer:

    def __init__(self, name, symbol, board, display, input_validator):
        self.__name = name
        self.__symbol = symbol
        self.board = board
        self.display = display
        self.input_validator = input_validator

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    def make_move(self):
        input = self.display.get_player_input()

        if self.input_validator.is_move_valid(input, self.board):
            player_input = int(input) - 1
            self.board.execute_move(player_input, self.symbol)
        else:
            self.display.print_invalid_move_message()
            self.make_move()
