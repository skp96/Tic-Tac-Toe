import unittest
from main import Board

class TicTacToeTests(unittest.TestCase):

    def test_testing_enviornment(self):
        self.assertEqual(True, True)

    def test_can_retrieve_moves_from_board(self):
        board = Board()
        result = board.retrieve_list_of_moves()
        expectation = [
            (1,1), (1,2), (1,3),
            (2,1), (2,2), (2,3),
            (3,1), (3,2), (3,3)
        ]
        self.assertEqual(result, expectation)
        

if __name__ == "__main__":
    unittest.main()