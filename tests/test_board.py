import pytest
from core_tic_tac_toe.board import Board


class TestBoard:

    @pytest.fixture
    def board(self):
        return Board()

    def test_board_can_retrieve_moves(self, board):
        result = board.retrieve_list_of_moves()
        expectation = [
            (1, 1), (1, 2), (1, 3),
            (2, 1), (2, 2), (2, 3),
            (3, 1), (3, 2), (3, 3)
        ]
        assert result == expectation

    def test_board_can_execute_move_to_first_position(self, board):
        result = board.execute_move(1, 1, "Ronald Graham")

        assert result == "Success"

    def test_board_can_execute_move_to_multiple_positions(self, board):
        result_1 = board.execute_move(1, 1, "Ronald Graham")
        result_2 = board.execute_move(3, 2, "Ronald Graham")
        result_3 = board.execute_move(2, 2, "Ronald Graham")

        assert result_1 == "Success"
        assert result_2 == "Success"
        assert result_3 == "Success"

    def test_format_board_into_readable_board(self, board):
        result = board.board_grid()
        expectation = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        assert result == expectation

    def test_format_board_into_readable_board_after_player_move(self, board):
        board.execute_move(1, 1, "Player 1")
        result = board.board_grid()
        expectation = ["Player 1", 2, 3, 4, 5, 6, 7, 8, 9]

        assert result == expectation
