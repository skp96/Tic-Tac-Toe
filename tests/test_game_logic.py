from core_tic_tac_toe import display
import pytest
from .mock_io import MockIo
from core_tic_tac_toe.human_player import HumanPlayer
from core_tic_tac_toe.board import Board
from core_tic_tac_toe.game_logic import GameLogic
from core_tic_tac_toe.display import Display


class TestGameLogic:

    @pytest.fixture(autouse=True)
    def board(self):
        return Board()

    @pytest.fixture
    def game_logic(self):
        return GameLogic()

    def test_player_wins_when_first_vertical_positions_taken(self, board, game_logic):
        mockIo = MockIo([1, 2, 3])
        display = Display(mockIo)
        player = HumanPlayer("Player", "X", board, display)

        player.make_move()
        player.make_move()
        player.make_move()

        grid = board.get_board()

        result = game_logic.check_winner(grid)

        assert result == True

    def test_player_wins_when_second_vertical_positions_taken(self, board, game_logic):
        mockIo = MockIo([4, 5, 6])
        display = Display(mockIo)
        player = HumanPlayer("Player", "O", board, display)

        player.make_move()
        player.make_move()
        player.make_move()

        grid = board.get_board()

        result = game_logic.check_winner(grid)

        assert result == True

    def test_player_wins_when_third_vertical_positions_taken(self, board, game_logic):
        mockIo = MockIo([8, 7, 9])
        display = Display(mockIo)
        player = HumanPlayer("Player", "O", board, display)

        player.make_move()
        player.make_move()
        player.make_move()

        grid = board.get_board()

        result = game_logic.check_winner(grid)

        assert result == True

    def test_player_does_not_win_when_no_vertical_positions_taken(self, board, game_logic):
        mockIo = MockIo([7, 8, 3])
        display = Display(mockIo)
        player = HumanPlayer("Player", "X", board, display)

        player.make_move()
        player.make_move()
        player.make_move()

        grid = board.get_board()

        result = game_logic.check_winner(grid)

        assert result == False

    def test_player_wins_when_first_horizontal_positions_taken(self, board, game_logic):
        mockIo = MockIo([4, 7, 1])
        display = Display(mockIo)
        player = HumanPlayer("Player", "X", board, display)

        player.make_move()
        player.make_move()
        player.make_move()

        grid = board.get_board()

        result = game_logic.check_winner(grid)

        assert result == True

    def test_player_wins_when_second_horizontal_positions_taken(self, board, game_logic):
        mockIo = MockIo([2, 5, 8])
        display = Display(mockIo)
        player = HumanPlayer("Player", "O", board, display)

        player.make_move()
        player.make_move()
        player.make_move()

        grid = board.get_board()

        result = game_logic.check_winner(grid)

        assert result == True

    def test_player_wins_when_third_horizontal_positions_taken(self, board, game_logic):
        mockIo = MockIo([3, 6, 9])
        display = Display(mockIo)
        player = HumanPlayer("Player", "", board, display)

        player.make_move()
        player.make_move()
        player.make_move()

        grid = board.get_board()

        result = game_logic.check_winner(grid)

        assert result == True

    def test_player_does_not_win_when_no_horizontal_positions_taken(self, board, game_logic):
        mockIo = MockIo([1, 5, 8])
        display = Display(mockIo)
        player = HumanPlayer("Player", "X", board, display)

        player.make_move()
        player.make_move()
        player.make_move()

        grid = board.get_board()

        result = game_logic.check_winner(grid)

        assert result == False

    def test_player_wins_when_first_diagonal_positions_taken(self, board, game_logic):
        mockIo = MockIo([5, 9, 1])
        display = Display(mockIo)
        player = HumanPlayer("Player", "X", board, display)

        player.make_move()
        player.make_move()
        player.make_move()

        grid = board.get_board()

        result = game_logic.check_winner(grid)

        assert result == True

    def test_player_wins_when_second_diagonal_positions_taken(self, board, game_logic):
        mockIo = MockIo([7, 3, 5])
        display = Display(mockIo)
        player = HumanPlayer("Player", "X", board, display)

        player.make_move()
        player.make_move()
        player.make_move()

        grid = board.get_board()

        result = game_logic.check_winner(grid)

        assert result == True

    def test_player_does_not_win_when_no_diagonal_positions_taken(self, board, game_logic):
        mockIo = MockIo([3, 5, 4])
        display = Display(mockIo)
        player = HumanPlayer("Player", "X", board, display)

        player.make_move()
        player.make_move()
        player.make_move()

        grid = board.get_board()

        result = game_logic.check_winner(grid)

        assert result == False

    def test_when_board_is_full_and_no_winner_expect_tie(self, board, game_logic):
        mock_io = MockIo([2, 1, 3, 6, 4, 7, 5, 8, 9])
        display = Display(mock_io)

        player_x = HumanPlayer("Player X", "X", board, display)
        player_o = HumanPlayer("Player O", "O", board, display)

        for _ in range(0, 5):
            player_x.make_move()

            if not mock_io.is_empty():
                player_o.make_move()

        grid = board.get_board()

        result = game_logic.is_tie(grid)

        assert result == True
