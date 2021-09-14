import unittest
from core_tic_tac_toe.board import Board
from core_tic_tac_toe.human_player import HumanPlayer

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.board = Board.build_board()
        self.player = HumanPlayer("Ronald Graham", self.board)

    def test_player_can_retrieve_moves_from_board(self):
        result = self.player.get_moves()
        expectation = [
            (1,1), (1,2), (1,3),
            (2,1), (2,2), (2,3),
            (3,1), (3,2), (3,3)
        ]

        self.assertEqual(result, expectation)

    def test_player_can_move_to_first_position(self):
        result = self.player.make_move("1,1")
        row, column, name = result

        self.assertEqual(name, "Ronald Graham")

    def test_player_cannot_move_to_invalid_position(self):
        self.player.make_move("1,1")

        result = self.player.make_move("1,1")

        self.assertEqual(result, "Invalid position")
