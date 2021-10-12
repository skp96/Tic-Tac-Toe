import pytest

from core_tic_tac_toe.easy_computer_player import EasyComputerPlayer
from core_tic_tac_toe.human_player import HumanPlayer
from core_tic_tac_toe.board import Board
from unittest import mock


class TestEasyComputerPlayer:

    @pytest.fixture
    def board(self):
        return Board()

    @pytest.fixture
    def computer_player(self, board):
        return EasyComputerPlayer(name="Easy Computer Player", player_marker="O", board=board)

    def test_expect_computer_to_be_initialized_with_correct_attributes(self, computer_player):
        assert computer_player.player_marker == "O"
        assert isinstance(computer_player.board, Board) == True

    def test_get_random_spot_returns_random_spot(self, computer_player, board):
        randomized_output = computer_player.get_random_spot()

        assert (randomized_output in board.get_board()) == True

    @mock.patch("core_tic_tac_toe.easy_computer_player.EasyComputerPlayer.get_random_spot", return_value=3)
    def test_expect_make_move_to_mark_board(self, mock_move_randomizer, computer_player, board):
        computer_player.make_move()

        ttt_board = board.get_board()

        assert ttt_board[3] == "O"
