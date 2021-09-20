from core_tic_tac_toe.board import Board
from core_tic_tac_toe.human_player import HumanPlayer


def board_test_script():
    board = Board()
    player = HumanPlayer("Player 1", board)

    player.make_move("1,1")
    player.make_move("2,2")
    player.make_move("3,3")
    result = board.retrieve_list_of_moves()
    print(result)


if __name__ == "__main__":
    board_test_script()
