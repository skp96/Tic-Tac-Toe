import pytest
from core_tic_tac_toe.board import Board

class TestBoard:
    
    @pytest.fixture
    def board(self):
        return Board()

    def test_board_can_retrieve_moves(self, board):
        result = board.retrieve_list_of_moves()
        expectation = [
            (1,1), (1,2), (1,3),
            (2,1), (2,2), (2,3),
            (3,1), (3,2), (3,3)
        ]
        assert result == expectation

    def test_board_can_execute_move_to_first_position(self, board):
        result = board.execute_move(1,1, "Ronald Graham")
        name = result[2]
        assert name == "Ronald Graham"

    def test_board_can_validate_move_for_first_position(self, board):
        result = board.valid_move(1,1)
        assert result == True

    def test_board_can_validate_moves(self, board):
        result_1 = board.valid_move(0,1)
        result_2 = board.valid_move(4,1)
        result_3 = board.valid_move(1,3)

        board.execute_move(2,3, "Ronald Graham")
        result_4 = board.valid_move(2,3)

        assert result_1 == False
        assert result_2 == False
        assert result_3 == True
        assert result_4 == False
        

    def test_board_can_execute_move_to_multiple_positions(self, board):
        result_1 = board.execute_move(1, 1, "Ronald Graham")
        result_2 = board.execute_move(3, 2, "Ronald Graham")
        result_3 = board.execute_move(2,2, "Ronald Graham")

        name_1 = result_1[2]
        name_2 = result_2[2]
        name_3 = result_3[2]

        assert name_1 == "Ronald Graham"
        assert name_2 == "Ronald Graham"
        assert name_3 == "Ronald Graham"
