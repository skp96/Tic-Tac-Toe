class Board:

    # builder methods for testing
    @classmethod
    def build_board(cls):
        return Board()




    def __init__(self):
        self.grid = [
            (1,1), (1,2), (1,3),
            (2,1), (2,2), (2,3),
            (3,1), (3,2), (3,3)
        ]

    def retrieve_list_of_moves(self):
        return self.grid

    def valid_move(self, row, column):
        for i in range(len(self.grid)):
            grid_row = self.grid[i][0]
            grid_column = self.grid[i][1]

            if grid_row == row and grid_column == column and len(self.grid[i]) == 2:
                return True

        return False
            

    def execute_move(self, row, column, player_name):
        move = None
        if self.valid_move(row, column):

            for i in range(len(self.grid)):
                grid_row = self.grid[i][0]
                grid_col = self.grid[i][1]

                if grid_row == row and grid_col == column:
                    self.grid[i] = (row, column, player_name)
                    move = self.grid[i]
                    break
        else:
            move = "Invalid position"
            
        return move
        
            
                

