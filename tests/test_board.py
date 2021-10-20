from unittest import mock
import pytest
from core_tic_tac_toe.board import Board


class TestBoard:

    @pytest.fixture
    def board(self):
        return Board()

    def test_board_can_retrieve_list_of_moves(self, board):
        result = board.retrieve_list_of_moves()
        expectation = [
            (1, 1), (1, 2), (1, 3),
            (2, 1), (2, 2), (2, 3),
            (3, 1), (3, 2), (3, 3)
        ]
        assert result == expectation

    def test_get_position(self, board):
        result = board.get_position(0)
        expectation = (1, 1)

        assert result == expectation

    def test_board_can_execute_move_to_first_position(self, board):
        input = 0
        board.execute_move(input, "Ronald Graham")

        result = board.get_position(input)

        assert len(result) == 3

    def test_board_can_execute_move_to_multiple_positions(self, board):
        input_1 = 0
        board.execute_move(input_1, "Ronald Graham")
        result_1 = board.get_position(input_1)

        input_2 = 7
        board.execute_move(input_2, "Ronald Graham")
        result_2 = board.get_position(input_2)

        input_3 = 4
        board.execute_move(input_3, "Ronald Graham")
        result_3 = board.get_position(input_3)

        assert len(result_1) == 3
        assert len(result_2) == 3
        assert len(result_3) == 3

    def test_can_get_readable_board(self, board):
        result = board.get_board()
        expectation = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        assert result == expectation

    def test_can_readable_board_include_symbol_after_move(self, board):
        board.execute_move(0, "X")

        result = board.get_board()
        expectation = ["X", 2, 3, 4, 5, 6, 7, 8, 9]

        assert result == expectation

    def test_can_readable_board_include_two_different_symbols_after_moves(self, board):
        board.execute_move(0, "X")
        board.execute_move(4, "O")

        result = board.get_board()
        expectation = ["X", 2, 3, 4, "O", 6, 7, 8, 9]

        assert result == expectation

    def test_can_readable_board_include_symbols_at_all_positions(self, board):
        for pos in range(0, 9):
            if pos % 2 == 0:
                board.execute_move(pos, "X")
            else:
                board.execute_move(pos, "O")

        result = board.get_board()
        expectation = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]

        assert result == expectation

    def test_for_valid_moves_valid_move_equals_true(self, board):
        result_1 = board.valid_move(0)
        result_2 = board.valid_move(5)
        result_3 = board.valid_move(8)

        assert result_1 == True
        assert result_2 == True
        assert result_3 == True

    def test_for_invalid_moves_valid_move_equals_false(self, board):
        result_1 = board.valid_move(-1)
        result_2 = board.valid_move(9)

        assert result_1 == False
        assert result_2 == False

    @mock.patch("core_tic_tac_toe.board.Board.get_board", return_value=[1, 2, "X", 4, "0", 6, 7, 8, 9])
    def test_get_available_position_indcies(self, mock_get_board, board):
        result = board.get_available_positions()

        assert result == [1, 2, 4, 6, 7, 8, 9]

    def test_get_horizontals_verticals_and_diagonals(self, board):
        horizontals_verticals_diagonals = [[1, 2, 3], [4, 5, 6], [
            7, 8, 9], [1, 4, 7, ], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

        result = board.get_all_positions()

        assert result == horizontals_verticals_diagonals
