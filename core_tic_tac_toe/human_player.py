class HumanPlayer:

    def __init__(self, name, mark, board):
        self.name = name
        self. mark = mark
        self.board = board

    def get_name(self):
        return self.name

    def get_mark(self):
        return self.mark

    def get_board(self):
        return self.board

    def make_move(self, position):
        row, column = [int(num) for num in position.split(",")]
        board = self.get_board()

        move = board.execute_move(row, column, self.get_mark())

        return move
