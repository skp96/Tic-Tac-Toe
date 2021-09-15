from core_tic_tac_toe.board import Board
from core_tic_tac_toe.human_player import HumanPlayer
import builtins

def board_test_script():
    input = builtins.input("Would you like to make a move to multiple positions: ")
    board = Board()
    player = HumanPlayer("Ronald Graham", board)

    if input.lower() == "yes":
        player.make_move("1,1")
        player.make_move("2,2")
        player.make_move("3,3")
        result = player.get_moves()
        print(result)
    elif input.lower() == "no":
        result = player.get_moves()
        print(result)
    else:
        board_test_script()

if __name__ == "__main__":
    board_test_script()


