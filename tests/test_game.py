import pytest
from core_tic_tac_toe.board import Board
from core_tic_tac_toe.display import Display
from .mock_io import MockIo
from core_tic_tac_toe.human_player import HumanPlayer
from core_tic_tac_toe.game import Game
from core_tic_tac_toe.game_logic import GameLogic
from core_tic_tac_toe.input_validator import InputValidator


class TestGame:

    @pytest.fixture
    def board(self):
        return Board()

    @pytest.fixture
    def game_logic(self):
        return GameLogic()

    @pytest.fixture
    def input_validator(self):
        return InputValidator()

    def test_a_player_wins_game_when_a_vertical_position_taken(self, board, game_logic, input_validator):
        mock_io = MockIo(["1", "4", "2", "8", "3"])
        display = Display(mock_io)
        player_1 = HumanPlayer("Player 1", "X", board,
                               display, input_validator)
        player_2 = HumanPlayer("Player 2", "0", board,
                               display, input_validator)

        game = Game(player_1=player_1, player_2=player_2,
                    display=display, board=board, game_logic=game_logic)

        game.start()
        current_player = game.get_current_player_name()
        display.announce_winner(current_player)

        assert mock_io.message == "We have a winner, congratulations Player 1"

    def test_a_player_wins_game_when_a_horizontal_position_taken(self, board, game_logic, input_validator):
        mock_io = MockIo(["1", "5", "3", "2", "7", "8"])
        display = Display(mock_io)
        player_1 = HumanPlayer("Player 1", "X", board,
                               display, input_validator)
        player_2 = HumanPlayer("Player 2", "0", board,
                               display, input_validator)

        game = Game(player_1=player_1, player_2=player_2,
                    display=display, board=board, game_logic=game_logic)

        game.start()
        current_player = game.get_current_player_name()
        display.announce_winner(current_player)

        assert mock_io.message == "We have a winner, congratulations Player 2"

    def test_a_player_wins_game_when_diagonal_positions_taken(self, board, game_logic, input_validator):
        mock_io = MockIo(["5", "1", "3", "2", "7"])
        display = Display(mock_io)
        player_1 = HumanPlayer("Player 1", "X", board,
                               display, input_validator)
        player_2 = HumanPlayer("Player 2", "0", board,
                               display, input_validator)

        game = Game(player_1=player_1, player_2=player_2,
                    display=display, board=board, game_logic=game_logic)

        game.start()
        current_player = game.get_current_player_name()
        display.announce_winner(current_player)

        assert mock_io.message == "We have a winner, congratulations Player 1"

    def test_expect_tie_game_when_board_full_and_no_winner(self, board, game_logic, input_validator):
        mock_io = MockIo(["2", "1", "3", "6", "4", "7", "5", "8", "9"])
        display = Display(mock_io)
        player_1 = HumanPlayer("Player 1", "X", board,
                               display, input_validator)
        player_2 = HumanPlayer("Player 2", "0", board,
                               display, input_validator)

        game = Game(player_1=player_1, player_2=player_2,
                    display=display, board=board, game_logic=game_logic)

        game.start()
        display.announce_tie()

        assert mock_io.message == "Good game, but it's a tie!"
