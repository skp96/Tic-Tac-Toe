import pytest
from core_tic_tac_toe.board import Board
from core_tic_tac_toe.human_player import HumanPlayer

class TestHumanPlayer:

    @pytest.fixture
    def board(self):
        return Board()
        
    @pytest.fixture
    def player(self, board):
        return HumanPlayer("Ronald Graham", board)

    @pytest.fixture
    def second_player(self, board):
        return HumanPlayer("Kanye West", board)


    def test_player_can_move_to_first_position(self, player):
        result = player.make_move("1,1")

        assert result == "Success"

    def test_player_can_move_to_multiple_positions(self, player):
        result_1 = player.make_move("1,3")
        result_2 = player.make_move("2,1")
        result_3 = player.make_move("3,2")

        assert result_1 == "Success"
        assert result_2 == "Success"
        assert result_3== "Success"

    def test_player_cannot_move_to_invalid_position_0_1(self, player):
        result = player.make_move("0,1")

        assert result == "Invalid position"

    def test_player_cannot_move_to_invalid_position_4_1(self, player):
        result = player.make_move("4,1")

        assert result == "Invalid position"

    def test_player_cannot_move_to_invalid_position_1_0(self, player):
        result = player.make_move("1,0")

        assert result == "Invalid position"
        
    def test_player_cannot_move_to_invalid_position_1_4(self, player):
        result = player.make_move("1,4")

        assert result == "Invalid position"
        
    def test_player_cannot_move_to_invalid_position_0_4(self, player):
        result = player.make_move("0,4")

        assert result == "Invalid position"

    def test_player_cannot_move_to_invalid_position_4_0(self, player):
        result = player.make_move("4,0")

        assert result == "Invalid position"

    def test_player_cannot_move_to_taken_positions(self, player, second_player):
        player.make_move("2,3")
        result_2 = second_player.make_move("2,3")

        assert result_2 == "Invalid position"

    def test_player_cannot_move_to_same_position(self, player):
        player.make_move("1,1")
        result_1 = player.make_move("1,1")

        assert result_1 == "Invalid position"

