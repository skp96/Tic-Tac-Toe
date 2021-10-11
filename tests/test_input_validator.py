import pytest
from core_tic_tac_toe.board import Board
from core_tic_tac_toe.input_validator import InputValidator


class TestInputValidator:

    @pytest.fixture
    def input_validator(self):
        return InputValidator()

    @pytest.fixture
    def board(self):
        return Board()

    def test_when_user_move_input_is_alphabetic_expect_false(self, input_validator, board):
        result_1 = input_validator.is_move_valid("A", board)
        result_2 = input_validator.is_move_valid("b", board)
        result_3 = input_validator.is_move_valid("bY", board)

        assert result_1 == False
        assert result_2 == False
        assert result_3 == False

    def test_when_user_move_input_is_special_characters_expect_false(self, input_validator, board):
        result_1 = input_validator.is_move_valid("\n", board)
        result_2 = input_validator.is_move_valid("@", board)
        result_3 = input_validator.is_move_valid("?", board)

        assert result_1 == False
        assert result_2 == False
        assert result_3 == False

    def test_when_user_move_input_contains_space_expect_false(self, input_validator, board):
        result_1 = input_validator.is_move_valid(" ", board)
        result_2 = input_validator.is_move_valid(" A", board)
        result_3 = input_validator.is_move_valid(" 1", board)

        assert result_1 == False
        assert result_2 == False
        assert result_3 == False

    def test_when_user_move_input_contains_float_expect_false(self, input_validator, board):
        result = input_validator.is_move_valid("1.5", board)

        assert result == False

    def test_when_user_move_input_contains_invalid_digit_expect_false(self, input_validator, board):
        result_1 = input_validator.is_move_valid("0", board)
        result_2 = input_validator.is_move_valid("10", board)

        assert result_1 == False
        assert result_2 == False
