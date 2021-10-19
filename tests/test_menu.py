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

    def test_menu_should_display_correct_options(self, menu, io):
        game_options = "1. Human vs Human\n 2. Human vs Easy Computer"
        menu.game_options(game_options)

        message = io.message

        assert message == "Please select from the following options:\n1. Human vs Human\n 2. Human vs Easy Computer"

    def test_expect_menu_to_return_selection_for_human_v_human(self, menu, io):
        game_options = "1. Human vs Human\n 2. Human vs Easy Computer"
        io.mock_user_input("1")
        result = menu.game_selection(game_options)

        assert result == "1"

    def test_expect_menu_to_return_selection_for_computer_v_computer(self, menu, io):
        game_options = "1. Human vs Human\n 2. Human vs Easy Computer"
        io.mock_user_input("2")
        result = menu.game_selection(game_options)

        assert result == "2"

    def test_expect_menu_to_keep_asking_for_game_selection_until_valid_input(self, menu, io):
        game_options = "1. Human vs Human\n 2. Human vs Easy Computer"
        io.mock_user_input("A")
        io.mock_user_input("")
        io.mock_user_input("$@")
        io.mock_user_input("1")

        result = menu.game_selection(game_options)

        assert result == "1"
