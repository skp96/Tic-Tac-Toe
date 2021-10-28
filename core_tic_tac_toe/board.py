import math


class Board:

    def __init__(self, size=3):
        self.__length = size * size
        self.__grid = self.__generate_grid(size)

    @property
    def length(self):
        return self.__length

    @property
    def grid(self):
        return self.__grid

    @grid.setter
    def grid(self, new_grid):
        self.__grid = new_grid

    def retrieve_list_of_moves(self):
        return self.grid

    def get_position(self, position):
        index = int(position) - 1
        return self.grid[index]

    def execute_move(self, position, player_symbol):
        index = int(position) - 1
        row, col = self.__get_position_data(index)

        self.grid[index] = (row, col, player_symbol)

    def undo_move(self, position):
        index = position - 1
        row, col, player_symbol = self.get_position(position)

        self.grid[index] = (row, col)

    def get_board(self):
        board_grid = []
        for pos in range(1, self.length + 1):
            pos_info = self.grid[pos - 1]

            if self.__position_not_taken(pos - 1):
                board_grid.append(pos)
            else:
                board_grid.append(pos_info[2])

        return board_grid

    def valid_move(self, position):
        index = int(position) - 1
        return self.__correct_position(index) and self.__position_not_taken(index)

    def get_available_positions(self):
        board = self.get_board()

        available_positions = [pos for pos in board if type(pos) == int]

        return available_positions

    def get_all_positions(self):
        board = self.get_board()
        board_length = len(board)
        vertical_horizontal_diagonal_length = int(math.sqrt(board_length))

        horizontals = self.__horizontal_positions(
            board, board_length, vertical_horizontal_diagonal_length)
        verticals = self.__vertical_positions(
            board, board_length, vertical_horizontal_diagonal_length)
        left_to_right_diagonals = self.__diagonal_left_to_right(
            board, board_length, vertical_horizontal_diagonal_length)
        right_to_left_diagonals = self.__diagonal_right_to_left(
            board, board_length, vertical_horizontal_diagonal_length)

        return [*horizontals, *verticals, left_to_right_diagonals, right_to_left_diagonals]

    def __correct_position(self, grid_pos):
        return grid_pos >= 0 and grid_pos < self.__length

    def __position_not_taken(self, grid_pos):
        try:
            return len(self.grid[grid_pos]) == 2
        except IndexError:
            return False

    def __get_position_data(self, index):
        row = self.grid[index][0]
        col = self.grid[index][1]

        return [row, col]

    def __horizontal_positions(self, board, board_length, horizontal_length):
        horizontal_positions = []

        horizontal_position = 0
        while horizontal_position < board_length:
            row = []

            row_start = horizontal_position
            row_end = row_start + horizontal_length

            for index in range(row_start, row_end):
                horizontal = board[index]
                row.append(horizontal)

            horizontal_positions.append(row)

            horizontal_position += horizontal_length

        return horizontal_positions

    def __vertical_positions(self, board, board_length, vertical_length):
        vertical_positions = []

        for vertical_pos in range(0, vertical_length):
            column = []

            index = vertical_pos

            while index < board_length:
                vertical = board[index]
                column.append(vertical)

                index += vertical_length

            vertical_positions.append(column)

        return vertical_positions

    def __diagonal_left_to_right(self, board, board_length, row_length):
        left_to_right_diagonals = []

        diagonal_pos = 0

        while diagonal_pos < board_length:

            diagonal = board[diagonal_pos]
            left_to_right_diagonals.append(diagonal)

            diagonal_pos += (row_length + 1)

        return left_to_right_diagonals

    def __diagonal_right_to_left(self, board, board_length, row_length):
        right_to_left_diagonals = []

        diagonal_pos = 0 + row_length - 1

        while diagonal_pos < board_length - 1:
            diagonal = board[diagonal_pos]
            right_to_left_diagonals.append(diagonal)

            diagonal_pos += (row_length - 1)

        return right_to_left_diagonals

    def __generate_grid(self, size):
        board = []

        for row in range(1, size + 1):
            for col in range(1, size + 1):
                coordinates = (row, col)
                board.append(coordinates)

        return board
