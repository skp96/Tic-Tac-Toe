import math


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
