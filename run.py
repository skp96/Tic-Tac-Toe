from main import Board
import builtins

def board_test_script():
    input = builtins.input("Would you like to make a move to postion 1,1: ")
    board = Board()

    if input.lower() == "yes":
        pass
    elif input.lower() == "no":
        result = board.grid
        print(result)
    else:
        board_test_script()

if __name__ == "__main__":
    board_test_script()


