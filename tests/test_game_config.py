from core_tic_tac_toe.board import Board
import pytest
from core_tic_tac_toe.display import Display
from .mock_io import MockIo
from core_tic_tac_toe.game_logic import GameLogic
from core_tic_tac_toe.input_validator import InputValidator
from core_tic_tac_toe.game_config import GameConfig
from core_tic_tac_toe.human_player import HumanPlayer
from core_tic_tac_toe.menu import Menu
from core_tic_tac_toe.easy_computer_player import EasyComputerPlayer
from core_tic_tac_toe.medium_computer_player import MediumComputerPlayer


class TestGameConfig:

    @pytest.fixture
    def board(self):
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    @pytest.fixture
    def io(self):
        return MockIo()

    @pytest.fixture
    def display(self, io):
        return Display(io)

    @pytest.fixture
    def game_logic(self):
        return GameLogic()

    @pytest.fixture
    def input_validator(self):
        return InputValidator()

    @pytest.fixture
    def menu(self, display, input_validator):
        return Menu(display=display, input_validator=input_validator)

    @pytest.fixture
    def game_config(self, display, game_logic, input_validator, menu):
        return GameConfig(display, game_logic, input_validator, menu)

    def test_can_initialize_game_config_with_correct_attributes(self, game_config):

        assert isinstance(game_config, GameConfig)

    def test_can_prepare_players_for_human_v_human(self, game_config, board):
        player_1, player_2 = game_config.prepare_players("1", board)

        assert isinstance(player_1, HumanPlayer)
        assert isinstance(player_2, HumanPlayer)

    def test_can_prepare_players_for_human_v_easy_computer(self, game_config, board):
        player_1, player_2 = game_config.prepare_players("2", board)

        assert isinstance(player_1, HumanPlayer)
        assert isinstance(player_2, EasyComputerPlayer)

    def test_can_prepare_players_for_human_v_medium_computer(self, game_config, board):
        player_1, player_2 = game_config.prepare_players("3", board)

        assert isinstance(player_1, HumanPlayer)
        assert isinstance(player_2, MediumComputerPlayer)

    def test_can_preare_board_for_game(self, game_config):
        board = game_config.prepare_board("4")

        assert isinstance(board, Board)
