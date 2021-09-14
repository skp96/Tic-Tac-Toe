import unittest
from core_tic_tac_toe.board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()
    
    def test_board_can_retrieve_moves(self):
        result = self.board.retrieve_list_of_moves()
        expectation = [
            (1,1), (1,2), (1,3),
            (2,1), (2,2), (2,3),
            (3,1), (3,2), (3,3)
        ]
        self.assertEqual(result, expectation)

    def test_board_can_execute_move_to_first_position(self):
        result = self.board.execute_move(1,1, "Ronald Graham")
        row, column, name = result
        self.assertEqual(name, "Ronald Graham")

    def test_board_can_validate_move_for_first_position(self):
        result = self.board.valid_move(1,1)
        self.assertEqual(result, True)
        