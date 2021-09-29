from core_tic_tac_toe.board import Board
from core_tic_tac_toe.human_player import HumanPlayer
from core_tic_tac_toe.display import Display


def display_empty_board_demo_script():
    board = Board()
    display = Display()

    moves = board.get_board()
    print("Empty board as seen in Figure 1\n")
    display.render(moves)
    print("\n")


def display_board_with_X_at_spot_1_demo_script():
    board = Board()
    display = Display()
    player_1 = HumanPlayer("Player 1", "X", board)

    player_1.make_move("1,1")
    moves = board.get_board()
    print("Board with X mark replacing spot 1, as seen in Figure 2\n")
    display.render(moves)
    print("\n")


def display_board_with_X_and_O_mark_demo_script():
    board = Board()
    player_1 = HumanPlayer("Player 1", "X", board)
    player_2 = HumanPlayer("Player 2", "O", board)
    display = Display()

    player_1.make_move("1,1")
    player_2.make_move("2,2")
    moves = board.get_board()
    print("Board with X mark at spot 1 and O mark at spot 5, as seen in Figure 3\n")
    display.render(moves)
    print("\n")


def display_board_with_X_at_all_spots_demo_script():
    board = Board()
    display = Display()
    player_1 = HumanPlayer("Player 1", "X", board)

    player_1.make_move("1,1")
    player_1.make_move("1,2")
    player_1.make_move("1,3")
    player_1.make_move("2,1")
    player_1.make_move("2,2")
    player_1.make_move("2,3")
    player_1.make_move("3,1")
    player_1.make_move("3,2")
    player_1.make_move("3,3")

    moves = board.get_board()
    print("Board with X mark at all spots, as seen in Figure 4\n")
    display.render(moves)


if __name__ == "__main__":
    display_empty_board_demo_script()
    display_board_with_X_at_spot_1_demo_script()
    display_board_with_X_and_O_mark_demo_script()
    display_board_with_X_at_all_spots_demo_script()
