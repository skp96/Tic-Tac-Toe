from core_tic_tac_toe.player import Player


class HumanPlayer(Player):

    def __init__(self, name, symbol, board, display, input_validator):
        super().__init__(name=name, symbol=symbol, board=board)
        self.display = display
        self.input_validator = input_validator

    def make_move(self):
        input = self.display.get_player_input()

        if self.input_validator.is_move_valid(input, self.board):
            self.board.execute_move(input, self.symbol)
        else:
            self.display.print_invalid_move_message()
            self.make_move()
