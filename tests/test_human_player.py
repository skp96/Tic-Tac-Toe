from core_tic_tac_toe import display
import pytest
from core_tic_tac_toe.board import Board
from core_tic_tac_toe.human_player import HumanPlayer
from .mock_io import MockIo
from core_tic_tac_toe.display import Display


class TestHumanPlayer:

    @pytest.fixture(scope="class")
    def mock_io(self):
        return MockIo(["1", "1", "2", "3"])

    @pytest.fixture
    def display(self, mock_io):
        return Display(mock_io)

    @pytest.fixture
    def board(self):
        return Board()

    def test_player_can_move_to_first_position(self, board, display):
        player = HumanPlayer("Player_1", "X", board, display)

        player.make_move()
        position = 1
        position_data = player.board.get_position(position - 1)

        assert position_data[2] == "X"

    def test_player_can_move_to_multiple_positions(self, board, display):
        player = HumanPlayer("Player_1", "X", board, display)

        player.make_move()
        position_1 = 1
        position_data = player.board.get_position(position_1 - 1)

        player.make_move()
        position_2 = 2
        position_data_2 = player.board.get_position(position_2 - 1)

        player.make_move()
        position_3 = 3
        position_data_3 = player.board.get_position(position_3 - 1)

        assert position_data[2] == "X"
        assert position_data_2[2] == "X"
        assert position_data_3[2] == "X"

    def test_player_cannot_move_to_invalid_position_0(self, board):
        mock_io = MockIo(["0", "1"])
        display = Display(mock_io)
        player = HumanPlayer("Player_1", "X", board, display)

        player.make_move()

        assert mock_io.message == "Invalid position, please try again!"

    def test_player_cannot_move_to_invalid_position_10_or_greater(self, board):
        mock_io = MockIo(["10", "11", "1"])
        display = Display(mock_io)
        player = HumanPlayer("Player_1", "X", board, display)

        player.make_move()

        assert mock_io.message == "Invalid position, please try again!"

    def test_player_cannot_move_to_taken_position(self, board):
        mock_io = MockIo(["1", "1", "2"])
        display = Display(mock_io)
        player_2 = HumanPlayer("Player_2", "O", board, display)
        player_1 = HumanPlayer("Player_1", "X", board, display)

        player_2.make_move()
        player_1.make_move()

        assert mock_io.message == "Invalid position, please try again!"

    def test_player_cannot_move_to_same_position(self, board):
        mock_io = MockIo(["1", "1", "2"])
        display = Display(mock_io)
        player = HumanPlayer("Player_1", "X", board, display)

        player.make_move()
        player.make_move()

        assert mock_io.message == "Invalid position, please try again!"
