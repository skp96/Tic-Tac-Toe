from core_tic_tac_toe import input_validator
from core_tic_tac_toe.board import Board
from core_tic_tac_toe.display import Display
from core_tic_tac_toe.io import Io
from core_tic_tac_toe.human_player import HumanPlayer
from core_tic_tac_toe.game import Game
from core_tic_tac_toe.game_logic import GameLogic
from core_tic_tac_toe.input_validator import InputValidator

if __name__ == "__main__":
    io = Io()
    display = Display(io)
    board = Board()
    game_logic = GameLogic()
    input_validator = InputValidator()
    player_1 = HumanPlayer("Player 1", "X", board, display, input_validator)
    player_2 = HumanPlayer("Player 2", "O", board, display, input_validator)

    game = Game(display=display, board=board,
                player_1=player_1, player_2=player_2, game_logic=game_logic)

    game.start()
