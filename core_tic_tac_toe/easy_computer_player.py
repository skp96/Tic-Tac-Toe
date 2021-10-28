from random import choice

from core_tic_tac_toe.player import Player


class EasyComputerPlayer(Player):
    def __init__(self, name, symbol, board):
        super().__init__(name=name, symbol=symbol, board=board)

    def get_random_spot(self):
        available_positions = self.board.get_available_positions()

        return choice(available_positions)

    def make_move(self):
        random_position = self.get_random_spot()

        self.board.execute_move(random_position - 1, self.symbol)
