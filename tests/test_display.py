import pytest
from core_tic_tac_toe.human_player import HumanPlayer
from core_tic_tac_toe.board import Board
from core_tic_tac_toe.display import Display
from .mock_io import MockIo
from core_tic_tac_toe.input_validator import InputValidator


class TestDisplay:

    @pytest.fixture(scope="class")
    def mock_io(self):
        return MockIo(["1", "1", "5", "9"])

    @pytest.fixture
    def board(self):
        return Board()

    @pytest.fixture
    def display(self, mock_io):
        return Display(mock_io)

    @pytest.fixture
    def input_validator(self):
        return InputValidator()

    def test_can_display_board(self, display, board, mock_io):
        moves = board.get_board()

        display.print_board(moves)

        expectation = (
            "     |     |    \n" +
            "  {}  |  {}  |  {} \n".format(1, 2, 3) +
            "     |     |    \n" +
            "-----------------\n" +
            "     |     |    \n" +
            "  {}  |  {}  |  {} \n".format(4, 5, 6) +
            "     |     |    \n" +
            "-----------------\n" +
            "     |     |    \n" +
            "  {}  |  {}  |  {} \n".format(7, 8, 9) +
            "     |     |    \n"
        )
        assert mock_io.message == expectation

    def test_display_board_after_player_moves_to_pos_1(self, display, board, mock_io, input_validator):
        player_1 = HumanPlayer("Player 1", "X", board,
                               display, input_validator)
        player_1.make_move()
        moves = board.get_board()

        display.print_board(moves)

        expectation = (
            "     |     |    \n" +
            "  {}  |  {}  |  {} \n".format("X", 2, 3) +
            "     |     |    \n" +
            "-----------------\n" +
            "     |     |    \n" +
            "  {}  |  {}  |  {} \n".format(4, 5, 6) +
            "     |     |    \n" +
            "-----------------\n" +
            "     |     |    \n" +
            "  {}  |  {}  |  {} \n".format(7, 8, 9) +
            "     |     |    \n"
        )
        assert mock_io.message == expectation

    def test_display_board_after_both_players_move_to_different_pos(self, display, board, mock_io, input_validator):
        player_1 = HumanPlayer("Player 1", "X", board,
                               display, input_validator)
        player_1.make_move()

        player_2 = HumanPlayer("Player 2", "O", board,
                               display, input_validator)
        player_2.make_move()
        moves = board.get_board()

        display.print_board(moves)

        expectation = (
            "     |     |    \n" +
            "  {}  |  {}  |  {} \n".format("X", 2, 3) +
            "     |     |    \n" +
            "-----------------\n" +
            "     |     |    \n" +
            "  {}  |  {}  |  {} \n".format(4, "O", 6) +
            "     |     |    \n" +
            "-----------------\n" +
            "     |     |    \n" +
            "  {}  |  {}  |  {} \n".format(7, 8, 9) +
            "     |     |    \n"
        )
        assert mock_io.message == expectation

    def test_display_board_after_both_players_move_to_same_position(self, board, input_validator):
        mock_io = MockIo(["8", "8", "1"])
        display = Display(mock_io)
        player_1 = HumanPlayer("Player 1", "X", board,
                               display, input_validator)
        player_1.make_move()

        player_2 = HumanPlayer("Player 2", "O", board,
                               display, input_validator)
        player_2.make_move()
        moves = board.get_board()

        display.print_board(moves)

        expectation = (
            "     |     |    \n" +
            "  {}  |  {}  |  {} \n".format("O", 2, 3) +
            "     |     |    \n" +
            "-----------------\n" +
            "     |     |    \n" +
            "  {}  |  {}  |  {} \n".format(4, 5, 6) +
            "     |     |    \n" +
            "-----------------\n" +
            "     |     |    \n" +
            "  {}  |  {}  |  {} \n".format(7, "X", 9) +
            "     |     |    \n"
        )

        assert mock_io.message == expectation

    def test_display_invalid_move_message(self, display, mock_io):
        display.print_invalid_move_message()

        assert mock_io.message == "Invalid position, please try again!"

    def test_display_can_retreive_player_input(self, display):
        result = display.get_player_input()

        assert result == "9"

    def test_can_display_player_turn(self, board, display, mock_io, input_validator):
        player = HumanPlayer("Test Player", "X", board,
                             display, input_validator)
        name = player.get_name()
        display.print_player_turn(name)

        assert mock_io.message == "Test Player it's your turn!"

    def test_can_display_winner_message(self, board, display, mock_io, input_validator):
        player = HumanPlayer("Test Player", "X", board,
                             display, input_validator)
        name = player.get_name()
        display.announce_winner(name)

        assert mock_io.message == "We have a winner, congratulations Test Player"

    def announce_tie(self, display, mock_io):
        display.announce_tie

        assert mock_io.message == "Good game, but it's a tie"
