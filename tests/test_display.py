import pytest
from core_tic_tac_toe.human_player import HumanPlayer
from core_tic_tac_toe.board import Board
from core_tic_tac_toe.display import Display
from .mock_io import MockIo


class TestDisplay:

    mockIo = MockIo(["1", "2", "5", "8", "8"])

    @pytest.fixture
    def board(self):
        return Board()

    @pytest.fixture
    def display(self):
        return Display()

    def test_can_display_board(self, display, board):
        moves = board.get_board()

        result = display.print_board(moves)

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
        assert result == expectation

    def test_display_board_after_player_moves_to_pos_1(self, display, board):
        mockIo = MockIo(["1"])
        player_1 = HumanPlayer("Player 1", "X", board, mockIo)
        player_1.make_move()
        moves = board.get_board()

        result = display.print_board(moves)

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
        assert result == expectation

    def test_display_board_after_both_players_move_to_different_pos(self, display, board):
        mockIo = MockIo(["1", "5"])
        player_1 = HumanPlayer("Player 1", "X", board, mockIo)
        player_1.make_move()

        player_2 = HumanPlayer("Player 2", "O", board, mockIo)
        player_2.make_move()
        moves = board.get_board()

        result = display.print_board(moves)

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
        assert result == expectation

    def test_display_board_after_both_players_move_to_same_position(self, display, board):
        mockIo = MockIo(["8", "8", "1"])
        player_1 = HumanPlayer("Player 1", "X", board, mockIo)
        player_1.make_move()

        player_2 = HumanPlayer("Player 2", "O", board, mockIo)
        player_2.make_move()
        moves = board.get_board()

        result = display.print_board(moves)

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

        assert result == expectation
