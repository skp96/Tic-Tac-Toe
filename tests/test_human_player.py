import pytest
from core_tic_tac_toe.board import Board
from core_tic_tac_toe.human_player import HumanPlayer
from .mock_io import MockIo


class TestHumanPlayer:

    @pytest.fixture
    def board(self):
        return Board()

    def test_player_can_move_to_first_position(self, board):
        mockIo = MockIo(["1"])
        player = HumanPlayer("Player_1", "X", board, mockIo)

        player.make_move()
        position_data = player.board.get_position(0)

        assert position_data[2] == "X"

    def test_player_can_move_to_multiple_positions(self, board):
        mockIo = MockIo(["1", "2", "3"])
        player = HumanPlayer("Player_1", "X", board, mockIo)

        player.make_move()
        position_data = player.board.get_position(0)

        player.make_move()
        position_data_2 = player.board.get_position(1)

        player.make_move()
        position_data_3 = player.board.get_position(2)

        assert position_data[2] == "X"
        assert position_data[2] == "X"
        assert position_data[2] == "X"

    def test_player_cannot_move_to_invalid_position_0(self, board):
        mockIo = MockIo([0, 1])
        player = HumanPlayer("Player_1", "X", board, mockIo)

        player.make_move()

        assert mockIo.message == "Invalid position, please try again!"

    def test_player_cannot_move_to_invalid_position_10_or_greater(self, board):
        mockIo = MockIo([10, 11, 1])
        player = HumanPlayer("Player_1", "X", board, mockIo)

        player.make_move()

        assert mockIo.message == "Invalid position, please try again!"

    def test_player_cannot_move_to_taken_position(self, board):
        mockIo_1 = MockIo([1, 2])
        mockIo_2 = MockIo([1])
        player_2 = HumanPlayer("Player_2", "O", board, mockIo_2)
        player_1 = HumanPlayer("Player_1", "X", board, mockIo_1)

        player_2.make_move()
        player_1.make_move()

        assert mockIo_1.message == "Invalid position, please try again!"

    def test_player_cannot_move_to_same_position(self, board):
        mockIo = MockIo([1, 1, 2])
        player = HumanPlayer("Player_1", "X", board, mockIo)

        player.make_move()
        player.make_move()

        assert mockIo.message == "Invalid position, please try again!"
