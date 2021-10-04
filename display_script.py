from core_tic_tac_toe.board import Board
from core_tic_tac_toe.human_player import HumanPlayer
from core_tic_tac_toe.display import Display
from core_tic_tac_toe.io import Io


def display_empty_board_demo_script():
    board = Board()
    display = Display()

    moves = board.get_board()
    print("\nEmpty board as seen in Figure 1\n")
    octothrope = display.print_board(moves)
    print(octothrope)


def display_board_with_X_at_spot_1_demo_script():
    board = Board()
    display = Display()
    io = Io()
    player_1 = HumanPlayer("Player 1", "X", board, io)

    player_1.make_move()
    moves = board.get_board()
    print("Board with X mark replacing spot 1, as seen in Figure 2\n")
    octothrope = display.print_board(moves)
    print(octothrope)


def display_board_with_X_and_O_mark_demo_script():
    board = Board()
    io = Io()
    player_1 = HumanPlayer("Player 1", "X", board, io)
    player_2 = HumanPlayer("Player 2", "O", board, io)
    display = Display()

    player_1.make_move()
    player_2.make_move()
    moves = board.get_board()
    print("Board with X mark at spot 1 and O mark at spot 5, as seen in Figure 3\n")
    octothrope = display.print_board(moves)
    print(octothrope)


def display_board_with_X_at_all_spots_demo_script():
    board = Board()
    io = Io()
    display = Display()
    player_1 = HumanPlayer("Player 1", "X", board, io)

    player_1.make_move()
    player_1.make_move()
    player_1.make_move()
    player_1.make_move()
    player_1.make_move()
    player_1.make_move()
    player_1.make_move()
    player_1.make_move()
    player_1.make_move()

    moves = board.get_board()
    print("Board with X mark at all spots, as seen in Figure 4\n")
    octothrope = display.print_board(moves)
    print(octothrope)


if __name__ == "__main__":
    display_empty_board_demo_script()
    display_board_with_X_at_spot_1_demo_script()
    display_board_with_X_and_O_mark_demo_script()
    display_board_with_X_at_all_spots_demo_script()
