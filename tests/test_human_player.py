from unittest import mock
import pytest
from core_tic_tac_toe.board import Board
from core_tic_tac_toe.human_player import HumanPlayer
from .mock_io import MockIo
from core_tic_tac_toe.display import Display
from core_tic_tac_toe.input_validator import InputValidator


class TestHumanPlayer:

    @pytest.fixture(scope="class")
    def mock_io(self):
        return MockIo()

    @pytest.fixture
    def display(self, mock_io):
        return Display(mock_io)

    @pytest.fixture
    def board(self):
        return Board()

    @pytest.fixture
    def input_validator(self):
        return InputValidator()

    def test_player_can_move_to_first_position(self, board, display, input_validator, mock_io):
        player = HumanPlayer("Player_1", "X", board, display, input_validator)
        mock_io.mock_user_input("1")
        player.make_move()
        position_data = player.board.get_position("1")

        assert position_data[2] == "X"

    def test_player_can_move_to_multiple_positions(self, board, display, input_validator, mock_io):
        player = HumanPlayer("Player_1", "X", board, display, input_validator)

        mock_io.mock_user_input("1")
        player.make_move()
        position_data = player.board.get_position("1")

        mock_io.mock_user_input("4")
        player.make_move()
        position_data_2 = player.board.get_position("4")

        mock_io.mock_user_input("7")
        player.make_move()
        position_data_3 = player.board.get_position("7")

        assert position_data[2] == "X"
        assert position_data_2[2] == "X"
        assert position_data_3[2] == "X"

    def test_player_cannot_move_to_invalid_position_0(self, board, input_validator, display, mock_io):
        player = HumanPlayer("Player_1", "X", board, display, input_validator)

        mock_io.mock_user_input("0")
        mock_io.mock_user_input("1")
        player.make_move()

        assert mock_io.message == "Invalid position, please try again!"

    def test_player_cannot_move_to_invalid_position_10_or_greater(self, board, input_validator):
        mock_io = MockIo(["10", "11", "1"])
        display = Display(mock_io)
        player = HumanPlayer("Player_1", "X", board, display, input_validator)

        player.make_move()

        assert mock_io.message == "Invalid position, please try again!"

    def test_player_cannot_move_to_taken_position(self, board, input_validator):
        mock_io = MockIo(["1", "1", "2"])
        display = Display(mock_io)
        player_2 = HumanPlayer("Player_2", "O", board,
                               display, input_validator)
        player_1 = HumanPlayer("Player_1", "X", board,
                               display, input_validator)

        player_2.make_move()
        player_1.make_move()

        assert mock_io.message == "Invalid position, please try again!"

    def test_player_cannot_move_to_same_position(self, board, input_validator):
        mock_io = MockIo(["1", "1", "2"])
        display = Display(mock_io)
        player = HumanPlayer("Player_1", "X", board, display, input_validator)

        player.make_move()
        player.make_move()

        assert mock_io.message == "Invalid position, please try again!"
