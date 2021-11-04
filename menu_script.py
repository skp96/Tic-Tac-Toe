from core_tic_tac_toe.board import Board
from core_tic_tac_toe.display import Display
from core_tic_tac_toe.game_config import GameConfig
from core_tic_tac_toe.io import Io
from core_tic_tac_toe.game_logic import GameLogic
from core_tic_tac_toe.menu import Menu
from core_tic_tac_toe.input_validator import InputValidator

if __name__ == "__main__":
    io = Io()
    display = Display(io)
    board = Board()
    game_logic = GameLogic()
    input_validator = InputValidator()
    menu = Menu(display=display, input_validator=input_validator)

    game_config = GameConfig(display, game_logic, input_validator, menu)

    game = game_config.prepare_game()
    game.start()
