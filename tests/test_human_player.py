import pytest
import random
from core_tic_tac_toe.board import Board
from core_tic_tac_toe.human_player import HumanPlayer

class TestHumanPlayer:

    @pytest.fixture
    def board(self):
        return Board.build_board()
        
    @pytest.fixture
    def player(self, board):
        return HumanPlayer("Ronald Graham", board)

    @pytest.fixture
    def second_player(self, board):
        return HumanPlayer("Kanye West", board)


    def test_player_can_retrieve_moves_from_board(self, player):
        result = player.get_moves()
        expectation = [
            (1,1), (1,2), (1,3),
            (2,1), (2,2), (2,3),
            (3,1), (3,2), (3,3)
        ]

        assert result == expectation

    def test_player_can_move_to_first_position(self, player):
        result = player.make_move("1,1")
        name = result[2]

        assert name == "Ronald Graham"

    def test_player_can_move_to_multiple_positions(self, player):
        result_1 = player.make_move("1,3")
        result_2 = player.make_move("2,1")
        result_3 = player.make_move("3,2")

        name_1 = result_1[2]
        name_2 = result_2[2]
        name_3 = result_3[2]

        assert name_1 == "Ronald Graham"
        assert name_2 == "Ronald Graham"
        assert name_3 == "Ronald Graham"

    def test_player_cannot_move_to_invalid_positions(self, player):
        result_1 = player.make_move("0,1")
        result_2 = player.make_move("4,1")
        result_3 = player.make_move("1,0")
        result_4 = player.make_move("1,4")
        result_5 = player.make_move("0,4")

        assert result_1 == "Invalid position"
        assert result_2 == "Invalid position"
        assert result_3 == "Invalid position"
        assert result_4 == "Invalid position"
        assert result_5 == "Invalid position"

    def test_player_cannot_move_to_taken_positions(self, player, second_player):
        player.make_move("1,1")
        result_1 = player.make_move("1,1")

        player.make_move("2,3")
        result_2 = second_player.make_move("2,3")

        assert result_1 == "Invalid position"
        assert result_2 == "Invalid position"
