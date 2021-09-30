class HumanPlayer:

    def __init__(self, name, symbol, board):
        self.name = name
        self.symbol = symbol
        self.board = board

    def get_name(self):
        return self.name

    def get_symbol(self):
        return self.symbol

    def get_board(self):
        return self.board

    def make_move(self, position):
        row, column = [int(num) for num in position.split(",")]
        board = self.get_board()

        move = board.execute_move(row, column, self.get_symbol())

        return move
