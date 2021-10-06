import pytest
from .mock_io import MockIo
from core_tic_tac_toe.human_player import HumanPlayer
from core_tic_tac_toe.board import Board
from core_tic_tac_toe.game_logic import GameLogic


class TestGameLogic:

    @pytest.fixture(autouse=True)
    def board(self):
        return Board()

    @pytest.fixture
    def game_logic(self):
        return GameLogic()

    def test_player_wins_when_first_vertical_positions_taken(self, board, game_logic):
        mockIo = MockIo([1, 2, 3])
        player = HumanPlayer("Player", "X", board, mockIo)

        player.make_move()
        player.make_move()
        player.make_move()

        grid = board.get_board()

        result = game_logic.is_winner(grid)

        assert result == True

    def test_player_wins_when_second_vertical_positions_taken(self, board, game_logic):
        mockIo = MockIo([4, 5, 6])
        player = HumanPlayer("Player", "O", board, mockIo)

        player.make_move()
        player.make_move()
        player.make_move()

        grid = board.get_board()

        result = game_logic.is_winner(grid)

        assert result == True

    def test_player_wins_when_third_vertical_positions_taken(self, board, game_logic):
        mockIo = MockIo([8, 7, 9])
        player = HumanPlayer("Player", "O", board, mockIo)

        player.make_move()
        player.make_move()
        player.make_move()

        grid = board.get_board()

        result = game_logic.is_winner(grid)

        assert result == True

    def test_player_does_not_win_when_no_vertical_positions_taken(self, board, game_logic):
        mockIo = MockIo([7, 8, 3])
        player = HumanPlayer("Player", "X", board, mockIo)

        player.make_move()
        player.make_move()
        player.make_move()

        grid = board.get_board()

        result = game_logic.is_winner(grid)

        assert result == False

    def test_player_wins_when_first_horizontal_positions_taken(self, board, game_logic):
        mockIo = MockIo([4, 7, 1])
        player = HumanPlayer("Player", "X", board, mockIo)

        player.make_move()
        player.make_move()
        player.make_move()

        grid = board.get_board()

        result = game_logic.is_winner(grid)

        assert result == True

    def test_player_wins_when_second_horizontal_positions_taken(self, board, game_logic):
        mockIo = MockIo([2, 5, 8])
        player = HumanPlayer("Player", "O", board, mockIo)

        player.make_move()
        player.make_move()
        player.make_move()

        grid = board.get_board()

        result = game_logic.is_winner(grid)

        assert result == True

    def test_player_wins_when_third_horizontal_positions_taken(self, board, game_logic):
        mockIo = MockIo([3, 6, 9])
        player = HumanPlayer("Player", "", board, mockIo)

        player.make_move()
        player.make_move()
        player.make_move()

        grid = board.get_board()

        result = game_logic.is_winner(grid)

        assert result == True

    def test_player_does_not_win_when_no_horizontal_positions_taken(self, board, game_logic):
        mockIo = MockIo([1, 5, 8])
        player = HumanPlayer("Player", "X", board, mockIo)

        player.make_move()
        player.make_move()
        player.make_move()

        grid = board.get_board()

        result = game_logic.is_winner(grid)

        assert result == False

    def test_player_wins_when_first_diagonal_positions_taken(self, board, game_logic):
        mockIo = MockIo([5, 9, 1])
        player = HumanPlayer("Player", "X", board, mockIo)

        player.make_move()
        player.make_move()
        player.make_move()

        grid = board.get_board()

        result = game_logic.is_winner(grid)

        assert result == True

    def test_player_wins_when_second_diagonal_positions_taken(self, board, game_logic):
        mockIo = MockIo([7, 3, 5])
        player = HumanPlayer("Player", "X", board, mockIo)

        player.make_move()
        player.make_move()
        player.make_move()

        grid = board.get_board()

        result = game_logic.is_winner(grid)

        assert result == True

    def test_player_does_not_win_when_no_diagonal_positions_taken(self, board, game_logic):
        mockIo = MockIo([3, 5, 4])
        player = HumanPlayer("Player", "X", board, mockIo)

        player.make_move()
        player.make_move()
        player.make_move()

        grid = board.get_board()

        result = game_logic.is_winner(grid)

        assert result == False

    def test_when_board_is_full_and_no_winner_expect_tie(self, board, game_logic):
        mock_io_x = MockIo([2, 3, 4, 5, 9])
        mock_io_0 = MockIo([1, 6, 7, 8])

        player_x = HumanPlayer("Player X", "X", board, mock_io_x)
        player_o = HumanPlayer("Player O", "O", board, mock_io_0)

        for _ in range(0, 5):
            player_x.make_move()

        for _ in range(0, 4):
            player_o.make_move()

        grid = board.get_board()

        result = game_logic.is_tie(grid)

        assert result == True
