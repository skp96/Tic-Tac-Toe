import pytest
from core_tic_tac_toe.board import Board
from core_tic_tac_toe.medium_computer_player import MediumComputerPlayer
from core_tic_tac_toe.game_logic import GameLogic


class TestMediumComputerPlayer:

    @pytest.fixture
    def board(self):
        return Board()

    @pytest.fixture
    def game_logic(self):
        return GameLogic()

    @pytest.fixture
    def medium_computer(self, board, game_logic):
        return MediumComputerPlayer("Medium Computer", "O", board, "X")

    def test_when_no_win_possible_expect_check_to_win_return_none(self, medium_computer, board):
        available_positions = board.get_available_positions()
        horizontals_verticals_diagonals = [[1, 2, 3], [4, 5, 6], [
            7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]

        result = medium_computer.check_for_win(
            horizontals_verticals_diagonals, "O", available_positions)

        assert result is None

    def test_when_win_possible_expect_check_to_win_return_9(self, medium_computer, board):
        available_positions = board.get_available_positions()
        horizontals_verticals_diagonals = [["O", "X", 3], [4, 5, 6], [7, 8, 9], [
            "X", "X", 7], [2, 5, 8], ["O", "O", 9], [1, 5, 9], [3, 5, 7]]

        result = medium_computer.check_for_win(
            horizontals_verticals_diagonals, "O", available_positions)

        assert result == 9

    def test_when_no_block_possible_check_to_block_return_none(self, medium_computer, board):
        available_positions = board.get_available_positions()
        horizontals_verticals_diagonals = [[1, 2, 3], [4, 5, 6], [
            7, 8, 9], [1, 4, 7], ["O", 5, 8], ["X", 6, 9], [1, 5, 9], [3, 5, 7]]

        result = medium_computer.check_for_win(
            horizontals_verticals_diagonals, "X", available_positions)

        assert result == None

    def test_when_block_possible_check_to_block_return_8(self, medium_computer, board):
        available_positions = board.get_available_positions()
        horizontals_verticals_diagonals = [["O", "O", 3], [4, 5, 6], [
            7, 8, 9], [1, 4, 7], ["X", "X", 8], ["X", 6, 9], [1, 5, 9], [3, 5, 7]]

        result = medium_computer.check_for_win(
            horizontals_verticals_diagonals, "X", available_positions)

        assert result == 8

    def test_when_win_possible_expect_make_move_to_mark_winning_position(self, medium_computer, board):
        board.execute_move(0, "O")
        board.execute_move(1, "O")

        medium_computer.make_move()

        ttt_board = board.get_board()
        print(ttt_board)

        assert ttt_board[2] == "O"

    def test_when_oppnent_win_possible_expect_make_move_to_block_position(self, medium_computer, board):
        board.execute_move(0, "X")
        board.execute_move(1, "X")

        medium_computer.make_move()

        ttt_board = board.get_board()

        assert ttt_board[2] == "O"

    def test_when_no_win_or_block_possible_expect_make_move_to_mark_first_available_position(self, medium_computer, board):
        medium_computer.make_move()

        ttt_board = board.get_board()

        assert ttt_board[0] == "O"
