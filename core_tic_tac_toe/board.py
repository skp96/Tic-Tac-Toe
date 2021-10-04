class Board:

    def __init__(self):
        self.grid = [
            (1, 1), (1, 2), (1, 3),
            (2, 1), (2, 2), (2, 3),
            (3, 1), (3, 2), (3, 3)
        ]

    def retrieve_list_of_moves(self):
        return self.grid

    def get_position(self, index):
        return self.grid[index]

    def execute_move(self, position, player_symbol):
        row, col = self.__get_position_data(position)

        self.grid[position] = (row, col, player_symbol)

    def get_board(self):
        board_grid = []

        for pos in range(1, 10):
            pos_info = self.grid[pos - 1]

            if self.__position_not_taken(pos - 1):
                board_grid.append(pos)
            else:
                board_grid.append(pos_info[2])

        return board_grid

    def valid_move(self, position):
        return self.__correct_position(position) and self.__position_not_taken(position)

    def __correct_position(self, grid_pos):
        return grid_pos >= 0 and grid_pos < 9

    def __position_not_taken(self, grid_pos):
        try:
            return len(self.grid[grid_pos]) == 2
        except IndexError:
            return False

    def __get_position_data(self, index):
        row = self.grid[index][0]
        col = self.grid[index][1]

        return [row, col]
