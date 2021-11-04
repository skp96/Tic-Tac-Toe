from unittest import mock
import pytest
from core_tic_tac_toe.human_player import HumanPlayer
from core_tic_tac_toe.board import Board
from core_tic_tac_toe.display import Display
from .mock_io import MockIo
from core_tic_tac_toe.input_validator import InputValidator


class TestDisplay:

    @pytest.fixture(scope="class")
    def mock_io(self):
        return MockIo()

    @pytest.fixture
    def board(self):
        return Board()

    @pytest.fixture
    def variable_board(self):
        return Board(5)

    @pytest.fixture
    def display(self, mock_io):
        return Display(mock_io)

    @pytest.fixture
    def input_validator(self):
        return InputValidator()

    def test_can_display_board(self, display, board, mock_io):
        moves = board.horizontal_positions()

        display.print_board(moves)

        expectation = (
            "          |          |          \n" +
            "{:>6}    |{:>6}    |     {}     \n".format(1, 2, 3) +
            "          |          |          \n" +
            "---------------------------------\n" +
            "          |          |          \n" +
            "{:>6}    |{:>6}    |     {}     \n".format(4, 5, 6) +
            "          |          |          \n" +
            "---------------------------------\n" +
            "          |          |          \n" +
            "{:>6}    |{:>6}    |     {}     \n".format(7, 8, 9) +
            "          |          |          \n"
        )
        assert mock_io.message == expectation

    def test_display_board_after_player_moves_to_pos_1(self, display, board, mock_io, input_validator):
        player_1 = HumanPlayer("Player 1", "X", board,
                               display, input_validator)

        mock_io.mock_user_input("1")

        player_1.make_move()
        moves = board.horizontal_positions()

        display.print_board(moves)

        expectation = (
            "          |          |          \n" +
            "{:>6}    |{:>6}    |     {}     \n".format("X", 2, 3) +
            "          |          |          \n" +
            "---------------------------------\n" +
            "          |          |          \n" +
            "{:>6}    |{:>6}    |     {}     \n".format(4, 5, 6) +
            "          |          |          \n" +
            "---------------------------------\n" +
            "          |          |          \n" +
            "{:>6}    |{:>6}    |     {}     \n".format(7, 8, 9) +
            "          |          |          \n"
        )
        assert mock_io.message == expectation

    def test_display_board_after_both_players_move_to_different_pos(self, display, board, mock_io, input_validator):
        player_1 = HumanPlayer("Player 1", "X", board,
                               display, input_validator)

        mock_io.mock_user_input("1")
        player_1.make_move()

        player_2 = HumanPlayer("Player 2", "O", board,
                               display, input_validator)

        mock_io.mock_user_input("5")
        player_2.make_move()
        moves = board.horizontal_positions()

        display.print_board(moves)

        expectation = (
            "          |          |          \n" +
            "{:>6}    |{:>6}    |     {}     \n".format("X", 2, 3) +
            "          |          |          \n" +
            "---------------------------------\n" +
            "          |          |          \n" +
            "{:>6}    |{:>6}    |     {}     \n".format(4, "O", 6) +
            "          |          |          \n" +
            "---------------------------------\n" +
            "          |          |          \n" +
            "{:>6}    |{:>6}    |     {}     \n".format(7, 8, 9) +
            "          |          |          \n"
        )
        assert mock_io.message == expectation

    def test_display_board_after_both_players_move_to_same_position(self, board, input_validator, display, mock_io):
        player_1 = HumanPlayer("Player 1", "X", board,
                               display, input_validator)
        mock_io.mock_user_input("8")
        player_1.make_move()

        player_2 = HumanPlayer("Player 2", "O", board,
                               display, input_validator)
        mock_io.mock_user_input("8")
        mock_io.mock_user_input("1")
        player_2.make_move()
        moves = board.horizontal_positions()

        display.print_board(moves)

        expectation = (
            "          |          |          \n" +
            "{:>6}    |{:>6}    |     {}     \n".format("O", 2, 3) +
            "          |          |          \n" +
            "---------------------------------\n" +
            "          |          |          \n" +
            "{:>6}    |{:>6}    |     {}     \n".format(4, 5, 6) +
            "          |          |          \n" +
            "---------------------------------\n" +
            "          |          |          \n" +
            "{:>6}    |{:>6}    |     {}     \n".format(7, "X", 9) +
            "          |          |          \n"
        )

        assert mock_io.message == expectation

    def test_display_invalid_move_message(self, display, mock_io):
        display.print_invalid_move_message()

        assert mock_io.message == "Invalid position, please try again!"

    def test_display_can_retreive_player_input(self, display, mock_io):
        mock_io.mock_user_input("9")
        result = display.get_player_input()

        assert result == "9"

    def test_can_display_player_turn(self, board, display, mock_io, input_validator):
        player = HumanPlayer("Test Player", "X", board,
                             display, input_validator)
        name = player.name
        display.print_player_turn(name)

        assert mock_io.message == "Test Player it's your turn!"

    def test_can_display_winner_message(self, board, display, mock_io, input_validator):
        player = HumanPlayer("Test Player", "X", board,
                             display, input_validator)
        name = player.name
        display.announce_winner(name)

        assert mock_io.message == "We have a winner, congratulations Test Player"

    def test_announce_tie(self, display, mock_io):
        display.announce_tie()

        assert mock_io.message == "Good game, but it's a tie!"

    def test_welcome_message(self, display, mock_io):
        display.welcome_message()

        assert mock_io.message == "Welcome to Tic Tac Toe\n"

    def test_game_options(self, display, mock_io):
        display.game_options("1. Human vs Human \n2. Human vs Easy Computer")

        assert mock_io.message == "1. Human vs Human \n2. Human vs Easy Computer"

    def test_print_invalid_game_selection_message(self, display, mock_io):
        display.print_invalid_game_selection_message()

        assert mock_io.message == "Invalid option, please try again!"

    def test_can_display_board_with_variable_size(self, display, variable_board, mock_io):
        moves = variable_board.horizontal_positions()

        display.print_board(moves)

        expectation = (
            "          |          |          |          |          \n" +
            "{:>6}    |{:>6}    |{:>6}    |{:>6}    |     {}     \n".format(1, 2, 3, 4, 5) +
            "          |          |          |          |          \n" +
            "-------------------------------------------------------\n" +
            "          |          |          |          |          \n" +
            "{:>6}    |{:>6}    |{:>6}    |{:>6}    |     {}     \n".format(6, 7, 8, 9, 10) +
            "          |          |          |          |          \n" +
            "-------------------------------------------------------\n" +
            "          |          |          |          |          \n" +
            "{:>6}    |{:>6}    |{:>6}    |{:>6}    |     {}     \n".format(11, 12, 13, 14, 15) +
            "          |          |          |          |          \n" +
            "-------------------------------------------------------\n" +
            "          |          |          |          |          \n" +
            "{:>6}    |{:>6}    |{:>6}    |{:>6}    |     {}     \n".format(16, 17, 18, 19, 20) +
            "          |          |          |          |          \n" +
            "-------------------------------------------------------\n" +
            "          |          |          |          |          \n" +
            "{:>6}    |{:>6}    |{:>6}    |{:>6}    |     {}     \n".format(21, 22, 23, 24, 25) +
            "          |          |          |          |          \n"
        )

        assert mock_io.message == expectation
