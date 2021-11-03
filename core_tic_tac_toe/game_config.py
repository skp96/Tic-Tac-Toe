from core_tic_tac_toe import game_logic
from .game import Game
from .human_player import HumanPlayer
from .easy_computer_player import EasyComputerPlayer
from .medium_computer_player import MediumComputerPlayer
from .hard_computer_player import HardComputerPlayer


class GameConfig:

    def __init__(self, board, display, game_logic, input_validator, menu):
        self.board = board
        self.display = display
        self.game_logic = game_logic
        self.input_validator = input_validator
        self.menu = menu
        self.game_options = "1. Human vs Human \n2. Human vs Easy Computer\n3. Human vs Medium Computer\n4. Human vs Hard Computer"

    def prepare_players(self, player_selection):

        if player_selection == "1":
            self.__prepare_human_players()
        elif player_selection == "2":
            self.__prepare_human_and_easy_computer_players()
        elif player_selection == "3":
            self.__prepare_human_and_medium_computer_players()
        elif player_selection == "4":
            self.__prepare_human_and_hard_computer_players()

    def prepare_game(self):
        self.display.welcome_message()
        game_selection = self.menu.game_selection(self.game_options)

        self.prepare_players(game_selection)

        game = Game(board=self.board, display=self.display,
                    game_logic=self.game_logic, player_1=self.player_1, player_2=self.player_2)

        return game

    def __prepare_human_players(self):
        self.player_1 = HumanPlayer(name="Player 1", symbol="X", board=self.board,
                                    display=self.display, input_validator=self.input_validator)

        self.player_2 = HumanPlayer(name="Player 2", symbol="O", board=self.board,
                                    display=self.display, input_validator=self.input_validator)

    def __prepare_human_and_easy_computer_players(self):
        self.player_1 = HumanPlayer(name="Player 1", symbol="X", board=self.board,
                                    display=self.display, input_validator=self.input_validator)

        self.player_2 = EasyComputerPlayer(
            name="Easy Computer", symbol="O", board=self.board)

    def __prepare_human_and_medium_computer_players(self):
        self.player_1 = HumanPlayer(name="Player 1", symbol="X", board=self.board,
                                    display=self.display, input_validator=self.input_validator)

        medium_computer_opponent = self.player_1.symbol

        self.player_2 = MediumComputerPlayer(
            name="Medium Computer", symbol="O", board=self.board, opponent_symbol=medium_computer_opponent)

    def __prepare_human_and_hard_computer_players(self):
        self.player_1 = HumanPlayer(name="Player 1", symbol="X", board=self.board,
                                    display=self.display, input_validator=self.input_validator)

        hard_computer_opponent = self.player_1.symbol

        self.player_2 = HardComputerPlayer(
            name="Hard Computer", symbol="O", board=self.board, opponent_symbol=hard_computer_opponent, game_logic=self.game_logic)
