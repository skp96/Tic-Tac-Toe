from random import choice


class EasyComputerPlayer:
    def __init__(self, name, player_marker, board):
        self.name = name
        self.player_marker = player_marker
        self.board = board

    def get_name(self):
        return self.name

    def get_symbol(self):
        return self.player_marker

    def get_random_spot(self):
        available_positions = self.board.get_available_positions()

        return choice(available_positions)

    def make_move(self):
        random_position = self.get_random_spot()

        self.board.execute_move(random_position, self.get_symbol())
