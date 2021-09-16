class Board:

    def __init__(self):
        self.grid = [
            (1,1), (1,2), (1,3),
            (2,1), (2,2), (2,3),
            (3,1), (3,2), (3,3)
        ]

    def retrieve_list_of_moves(self):
        return self.grid
            
    def execute_move(self, row, column, player_name):
        if self.__valid_move(row, column):

            for grid_pos in range(len(self.grid)):

                if self.__correct_position(row, column, grid_pos):
                    self.grid[grid_pos] = (row, column, player_name)
                    return "Success"
        else:
            return "Invalid position"
            

    # Private Methods

    def __valid_move(self, row, column):
        for grid_pos in range(len(self.grid)):

            if self.__correct_position(row, column, grid_pos) and self.__position_not_taken(grid_pos):
                return True

        return False

    def __correct_position(self, row, column, grid_pos):
        grid_row = self.grid[grid_pos][0]
        grid_col = self.grid[grid_pos][1]

        return grid_row == row and grid_col == column

    def __position_not_taken(self, grid_pos):
        return len(self.grid[grid_pos]) == 2
        
            
                

