import pytest
from core_tic_tac_toe.human_player import HumanPlayer
from core_tic_tac_toe.board import Board
from core_tic_tac_toe.display import Display


class TestDisplay:

    @pytest.fixture
    def board(self):
        return Board()

    @pytest.fixture
    def player_1(self, board):
        return HumanPlayer("Player 1", "X", board)

    @pytest.fixture
    def player_2(self, board):
        return HumanPlayer("Player 2", "O", board)

    @pytest.fixture
    def display(self):
        return Display()

    def test_can_display_board(self, capsys, display, board):
        moves = board.get_board()
        display.render(moves)
        result = capsys.readouterr()

        expectation = (
            "    |    |    \n" +
            " {}  | {}  | {} \n".format(1, 2, 3) +
            "    |    |    \n" +
            "--------------\n" +
            "    |    |    \n" +
            " {}  | {}  | {} \n".format(4, 5, 6) +
            "    |    |    \n" +
            "--------------\n" +
            "    |    |    \n" +
            " {}  | {}  | {} \n".format(7, 8, 9) +
            "    |    |    \n"
        )
        assert result.out == expectation

    def test_display_board_after_player_moves_to_pos_1(self, capsys, display, player_1, board):
        player_1.make_move("1,1")
        moves = board.get_board()

        display.render(moves)

        result = capsys.readouterr()
        expectation = (
            "    |    |    \n" +
            " {}  | {}  | {} \n".format("X", 2, 3) +
            "    |    |    \n" +
            "--------------\n" +
            "    |    |    \n" +
            " {}  | {}  | {} \n".format(4, 5, 6) +
            "    |    |    \n" +
            "--------------\n" +
            "    |    |    \n" +
            " {}  | {}  | {} \n".format(7, 8, 9) +
            "    |    |    \n"
        )
        assert result.out == expectation

    def test_display_board_after_both_players_move_to_different_pos(self, capsys, display, player_1, player_2, board):
        player_1.make_move("1,1")
        player_2.make_move("2,2")
        moves = board.get_board()

        display.render(moves)

        result = capsys.readouterr()
        expectation = (
            "    |    |    \n" +
            " {}  | {}  | {} \n".format("X", 2, 3) +
            "    |    |    \n" +
            "--------------\n" +
            "    |    |    \n" +
            " {}  | {}  | {} \n".format(4, "O", 6) +
            "    |    |    \n" +
            "--------------\n" +
            "    |    |    \n" +
            " {}  | {}  | {} \n".format(7, 8, 9) +
            "    |    |    \n"
        )
        assert result.out == expectation

    def test_display_board_after_both_players_move_to_same_position(self, capsys, display, player_1, player_2, board):
        player_1.make_move("3,2")
        player_2.make_move("3,2")
        moves = board.get_board()

        display.render(moves)

        result = capsys.readouterr()
        expectation = (
            "    |    |    \n" +
            " {}  | {}  | {} \n".format(1, 2, 3) +
            "    |    |    \n" +
            "--------------\n" +
            "    |    |    \n" +
            " {}  | {}  | {} \n".format(4, 5, 6) +
            "    |    |    \n" +
            "--------------\n" +
            "    |    |    \n" +
            " {}  | {}  | {} \n".format(7, "X", 9) +
            "    |    |    \n"
        )

        assert result.out == expectation
