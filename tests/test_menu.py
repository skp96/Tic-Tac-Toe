from core_tic_tac_toe.human_player import HumanPlayer
import pytest
from .mock_io import MockIo
from core_tic_tac_toe.display import Display
from core_tic_tac_toe.input_validator import InputValidator
from core_tic_tac_toe.menu import Menu


class TestMenu:

    @pytest.fixture
    def io(self):
        return MockIo()

    @pytest.fixture
    def display(self, io):
        return Display(io)

    @pytest.fixture
    def input_validator(self):
        return InputValidator()

    @pytest.fixture
    def menu(self, display, input_validator):
        return Menu(display=display, input_validator=input_validator)

    def test_expect_menu_to_be_initialized_with_correct_attributes(self, menu):

        assert isinstance(menu.display, Display)
        assert isinstance(menu.input_validator, InputValidator)

    def test_menu_should_display_option_human_v_human(self, menu, io):
        menu.game_options()

        message = io.message

        assert message == "1. Human vs Human"

    def test_expect_menu_to_process_player_names_for_human_v_human(self, menu, io):
        io.mock_user_input("1")
        result = menu.game_selection()

        assert result == "1"

    def test_expect_menu_to_keep_asking_for_game_selection_until_valid_input(self, menu, io):
        io.mock_user_input("A")
        io.mock_user_input("")
        io.mock_user_input("$@")
        io.mock_user_input("1")

        result = menu.game_selection()

        assert result == "1"

    def test_expect_menu_to_prepare_players_when_human_v_human(self, menu, io):
        io.mock_user_input("1")
        result = menu.prep_players()

        player_1, player_2 = result

        assert isinstance(player_1, HumanPlayer) == True
        assert isinstance(player_2, HumanPlayer) == True
