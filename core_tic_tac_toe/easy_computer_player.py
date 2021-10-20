from random import choice


class EasyComputerPlayer:
    def __init__(self, name, symbol, board):
        self.__name = name
        self.__symbol = symbol
        self.board = board

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    def get_random_spot(self):
        available_positions = self.board.get_available_positions()

        return choice(available_positions)

    def make_move(self):
        random_position = self.get_random_spot()

        self.board.execute_move(random_position - 1, self.symbol)
