from unittest import mock
import pytest
from core_tic_tac_toe.board import Board


class TestBoard:

    @pytest.fixture
    def board(self):
        return Board()

    @pytest.fixture
    def board_size_5(self):
        return Board(5)

    def test_board_can_retrieve_list_of_moves(self, board):
        result = board.retrieve_list_of_moves()
        expectation = [
            (1, 1), (1, 2), (1, 3),
            (2, 1), (2, 2), (2, 3),
            (3, 1), (3, 2), (3, 3)
        ]
        assert result == expectation

    def test_board_can_retrieve_list_of_moves_for_board_size_5(self, board_size_5):
        result = board_size_5.retrieve_list_of_moves()
        expectation = [
            (1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
            (2, 1), (2, 2), (2, 3), (2, 4), (2, 5),
            (3, 1), (3, 2), (3, 3), (3, 4), (3, 5),
            (4, 1), (4, 2), (4, 3), (4, 4), (4, 5),
            (5, 1), (5, 2), (5, 3), (5, 4), (5, 5)
        ]
        assert result == expectation

    def test_get_position(self, board):
        result = board.get_position("1")
        expectation = (1, 1)

        assert result == expectation

    def test_get_position_for_board_size_5(self, board_size_5):
        result = board_size_5.get_position("16")
        expectation = (4, 1)

        assert result == expectation

    def test_board_can_execute_move_to_first_position(self, board):
        input = "1"
        board.execute_move(input, "Ronald Graham")

        result = board.get_position(input)

        assert len(result) == 3

    def test_board_can_execute_move_to_first_position_for_board_size_5(self, board_size_5):
        input = "1"
        board_size_5.execute_move(input, "Ronald Graham")

        result = board_size_5.get_position(input)

        assert len(result) == 3

    def test_board_can_execute_move_to_multiple_positions(self, board):
        input_1 = "1"
        board.execute_move(input_1, "Ronald Graham")
        result_1 = board.get_position(input_1)

        input_2 = "8"
        board.execute_move(input_2, "Ronald Graham")
        result_2 = board.get_position(input_2)

        input_3 = "4"
        board.execute_move(input_3, "Ronald Graham")
        result_3 = board.get_position(input_3)

        assert len(result_1) == 3
        assert len(result_2) == 3
        assert len(result_3) == 3

    def test_board_can_execute_move_to_multiple_positions_for_board_size_5(self, board_size_5):
        input_1 = "14"
        board_size_5.execute_move(input_1, "Ronald Graham")
        result_1 = board_size_5.get_position(input_1)

        input_2 = "10"
        board_size_5.execute_move(input_2, "Ronald Graham")
        result_2 = board_size_5.get_position(input_2)

        input_3 = "25"
        board_size_5.execute_move(input_3, "Ronald Graham")
        result_3 = board_size_5.get_position(input_3)

        assert len(result_1) == 3
        assert len(result_2) == 3
        assert len(result_3) == 3

    def test_can_get_readable_board(self, board):
        result = board.get_board()
        expectation = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        assert result == expectation

    def test_can_get_readable_board_for_board_size_5(self, board_size_5):
        result = board_size_5.get_board()
        expectation = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                       13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

        assert result == expectation

    def test_can_readable_board_include_symbol_after_move(self, board):
        board.execute_move("1", "X")

        result = board.get_board()
        expectation = ["X", 2, 3, 4, 5, 6, 7, 8, 9]

        assert result == expectation

    def test_can_readable_board_include_symbol_after_move_for_board_size_5(self, board_size_5):
        board_size_5.execute_move("12", "X")

        result = board_size_5.get_board()
        expectation = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, "X",
                       13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

        assert result == expectation

    def test_can_readable_board_include_two_different_symbols_after_moves(self, board):
        board.execute_move("1", "X")
        board.execute_move("5", "O")

        result = board.get_board()
        expectation = ["X", 2, 3, 4, "O", 6, 7, 8, 9]

        assert result == expectation

    def test_can_readable_board_include_two_different_symbols_after_moves_for_board_size_5(self, board_size_5):
        board_size_5.execute_move("18", "X")
        board_size_5.execute_move("19", "O")

        result = board_size_5.get_board()
        expectation = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                       13, 14, 15, 16, 17, "X", "O", 20, 21, 22, 23, 24, 25]

        assert result == expectation

    def test_can_readable_board_include_symbols_at_all_positions(self, board):
        for pos in range(0, board.length):
            if pos % 2 == 0:
                board.execute_move(str(pos + 1), "X")
            else:
                board.execute_move(str(pos + 1), "O")

        result = board.get_board()
        expectation = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]

        assert result == expectation

    def test_can_readable_board_include_symbols_at_all_positions_for_board_size_5(self, board_size_5):
        for pos in range(0, board_size_5.length):
            if pos % 2 == 0:
                board_size_5.execute_move(str(pos + 1), "X")
            else:
                board_size_5.execute_move(str(pos + 1), "O")

        result = board_size_5.get_board()
        expectation = ["X", "O", "X", "O", "X", "O", "X", "O", "X", "O", "X", "O",
                       "X", "O", "X", "O", "X", "O", "X", "O", "X", "O", "X", "O", "X"]

        assert result == expectation

    def test_for_valid_moves_valid_move_equals_true(self, board):
        result_1 = board.valid_move("1")
        result_2 = board.valid_move("5")
        result_3 = board.valid_move("9")

        assert result_1 == True
        assert result_2 == True
        assert result_3 == True

    def test_for_valid_moves_valid_move_equals_true_for_board_size_5(self, board_size_5):
        result_1 = board_size_5.valid_move("18")
        result_2 = board_size_5.valid_move("23")
        result_3 = board_size_5.valid_move("12")

        assert result_1 == True
        assert result_2 == True
        assert result_3 == True

    def test_for_invalid_moves_valid_move_equals_false(self, board):
        result_1 = board.valid_move("-1")
        result_1 = board.valid_move("0")
        result_2 = board.valid_move("10")

        assert result_1 == False
        assert result_2 == False

    def test_for_invalid_moves_valid_move_equals_false_for_board_size_5(self, board_size_5):
        result_1 = board_size_5.valid_move("-1")
        result_1 = board_size_5.valid_move("0")
        result_2 = board_size_5.valid_move("26")

        assert result_1 == False
        assert result_2 == False

    @mock.patch("core_tic_tac_toe.board.Board.get_board", return_value=[1, 2, "X", 4, "0", 6, 7, 8, 9])
    def test_get_available_position_indcies(self, mock_get_board, board):
        result = board.get_available_positions()

        assert result == [1, 2, 4, 6, 7, 8, 9]

    @mock.patch("core_tic_tac_toe.board.Board.get_board", return_value=["X", "O", "X", "O", 5, 6, "X", "O", 11, 12,
                                                                        13, "X", "O", 16, 17, "X", "O", 20, 21, 22, 23, 24, 25])
    def test_get_available_position_indcies_for_board_size_5(self, mock_get_board, board_size_5):
        result = board_size_5.get_available_positions()

        assert result == [5, 6, 11, 12, 13, 16, 17, 20, 21, 22, 23, 24, 25]

    def test_get_horizontals_verticals_and_diagonals(self, board):
        horizontals_verticals_diagonals = [[1, 2, 3], [4, 5, 6], [
            7, 8, 9], [1, 4, 7, ], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

        result = board.get_all_positions()

        assert result == horizontals_verticals_diagonals

    def test_get_horizontals_verticals_and_diagonals_for_board_size_5(self, board_size_5):
        horizontals_verticals_diagonals = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15, ], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [
            1, 6, 11, 16, 21], [2, 7, 12, 17, 22], [3, 8, 13, 18, 23], [4, 9, 14, 19, 24], [5, 10, 15, 20, 25], [1, 7, 13, 19, 25], [5, 9, 13, 17, 21]]

        result = board_size_5.get_all_positions()

        assert result == horizontals_verticals_diagonals

    def test_undo_move_execution(self, board):
        board.execute_move("1", "X")
        executed_postion = board.get_position("1")

        board.undo_move(1)
        original_position = board.get_position(0)

        assert len(original_position) != len(executed_postion)

    def test_undo_move_execution_for_board_size_5(self, board_size_5):
        board_size_5.execute_move("10", "X")
        executed_postion = board_size_5.get_position("10")

        board_size_5.undo_move(10)
        original_position = board_size_5.get_position(10)

        assert len(original_position) != len(executed_postion)
