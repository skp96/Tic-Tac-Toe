from core_tic_tac_toe.board import Board
from core_tic_tac_toe.human_player import HumanPlayer
from core_tic_tac_toe.display import Display


def display_test_script():
    board = Board()
    player_1 = HumanPlayer("Player 1", "X", board)
    player_2 = HumanPlayer("Player 2", "O", board)

    display = Display()

    moves = board.get_board()
    display.render(moves)

    # player_1.make_move("1,1")
    # moves = board.get_board()
    # display.render(moves)

    # player_1.make_move("1,1")
    # player_2.make_move("2,2")
    # moves = board.get_board()
    # display.render(moves)

    # player_1.make_move("1,1")
    # player_1.make_move("1,2")
    # player_1.make_move("1,3")
    # player_1.make_move("2,1")
    # player_1.make_move("2,2")
    # player_1.make_move("2,3")
    # player_1.make_move("3,1")
    # player_1.make_move("3,2")
    # player_1.make_move("3,3")

    # moves = board.get_board()
    # display.render(moves)


if __name__ == "__main__":
    display_test_script()
