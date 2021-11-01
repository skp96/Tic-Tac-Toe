from core_tic_tac_toe import game_logic
import pytest
from core_tic_tac_toe.board import Board
from core_tic_tac_toe.game_logic import GameLogic
from core_tic_tac_toe.hard_computer_player import HardComputerPlayer


class TestHardComputerPlayer:

    @pytest.fixture
    def board(self):
        return Board()

    @pytest.fixture
    def game_logic(self):
        return GameLogic()

    @pytest.fixture
    def hard_computer_player(self, board, game_logic):
        return HardComputerPlayer("Hard Computer", "O", "X", board, game_logic)

    def test_will_take_winning_position_3(self, board, hard_computer_player):
        board.grid = [
            (1, 1, "O"), (1, 2, "O"), (1, 3),
            (2, 1, "X"), (2, 2), (2, 3, "X"),
            (3, 1), (3, 2), (3, 3, "X")
        ]
        hard_computer_player.make_move()

        expectation = [
            (1, 1, "O"), (1, 2, "O"), (1, 3, "O"),
            (2, 1, "X"), (2, 2), (2, 3, "X"),
            (3, 1), (3, 2), (3, 3, "X")
        ]

        assert board.grid == expectation

    def test_will_block_opponent_from_winning(self, board, hard_computer_player):
        board.grid = [
            (1, 1, "X"), (1, 2, "O"), (1, 3),
            (2, 1), (2, 2, "X"), (2, 3),
            (3, 1), (3, 2), (3, 3)
        ]
        hard_computer_player.make_move()

        expectation = [
            (1, 1, "X"), (1, 2, "O"), (1, 3),
            (2, 1), (2, 2, "X"), (2, 3),
            (3, 1), (3, 2), (3, 3, "O")
        ]

        assert board.grid == expectation

    def test_will_win_over_block(self, board, hard_computer_player):
        board.grid = [
            (1, 1, "X"), (1, 2, "X"), (1, 3),
            (2, 1, "O"), (2, 2, "O"), (2, 3),
            (3, 1), (3, 2, "X"), (3, 3)
        ]
        hard_computer_player.make_move()

        expectation = [
            (1, 1, "X"), (1, 2, "X"), (1, 3),
            (2, 1, "O"), (2, 2, "O"), (2, 3, "O"),
            (3, 1), (3, 2, "X"), (3, 3)
        ]

        assert board.grid == expectation

    def test_computer_will_select_optimal_corners_if_oppnenet_selects_center(self, board, hard_computer_player):
        board.grid = [
            (1, 1), (1, 2), (1, 3),
            (2, 1), (2, 2, "X"), (2, 3),
            (3, 1), (3, 2), (3, 3)
        ]

        hard_computer_player.make_move()

        expectation_1 = [
            (1, 1, "O"), (1, 2), (1, 3),
            (2, 1), (2, 2, "X"), (2, 3),
            (3, 1), (3, 2), (3, 3)
        ]

        expectation_2 = [
            (1, 1), (1, 2), (1, 3, "O"),
            (2, 1), (2, 2, "X"), (2, 3),
            (3, 1), (3, 2), (3, 3)
        ]

        expectation_3 = [
            (1, 1), (1, 2), (1, 3),
            (2, 1), (2, 2, "X"), (2, 3),
            (3, 1, "O"), (3, 2), (3, 3)
        ]
        expectation_4 = [
            (1, 1), (1, 2), (1, 3),
            (2, 1), (2, 2, "X"), (2, 3),
            (3, 1), (3, 2), (3, 3, "O")
        ]

        assert board.grid == expectation_1 or board.grid == expectation_2 or board.grid == expectation_3 or board.grid == expectation_4

    def test_computer_will_select_center_if_opponent_selects_a_corner(self, board, hard_computer_player):
        board.grid = [
            (1, 1), (1, 2), (1, 3),
            (2, 1), (2, 2), (2, 3),
            (3, 1, "X"), (3, 2), (3, 3)
        ]

        hard_computer_player.make_move()

        expectation = [
            (1, 1), (1, 2), (1, 3),
            (2, 1), (2, 2, "O"), (2, 3),
            (3, 1, "X"), (3, 2), (3, 3,)
        ]

        assert board.grid == expectation
