class HumanPlayer:
    
    def __init__(self, name, board):
        self.name = name
        self.board = board

    def make_move(self, position):
        row, column = [int(num) for num in position.split(",")]

        move = self.board.execute_move(row, column, self.name)

        return move

    def get_moves(self):
        return self.board.retrieve_list_of_moves()

        

        