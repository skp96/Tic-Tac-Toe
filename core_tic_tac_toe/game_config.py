from core_tic_tac_toe.board import Board
from .game import Game
from .human_player import HumanPlayer
from .easy_computer_player import EasyComputerPlayer
from .medium_computer_player import MediumComputerPlayer
from .hard_computer_player import HardComputerPlayer


class GameConfig:

    def __init__(self, display, game_logic, input_validator, menu):
        self.display = display
        self.game_logic = game_logic
        self.input_validator = input_validator
        self.menu = menu
        self.player_game_options = "1. Human vs Human \n2. Human vs Easy Computer\n3. Human vs Medium Computer\n4. Human vs Hard Computer"
        self.board_option = "What size board would you like to play on? Enter a value between 3 to 9 (e.g 3 will generate a 3X3 board)"

    def prepare_players(self, player_selection, board):

        if player_selection == "1":
            return self.__prepare_human_players(board)
        elif player_selection == "2":
            return self.__prepare_human_and_easy_computer_players(board)
        elif player_selection == "3":
            return self.__prepare_human_and_medium_computer_players(board)
        elif player_selection == "4":
            return self.__prepare_human_and_hard_computer_players(board)

    def prepare_board(self, board_size):
        return Board(board_size)

    def prepare_game(self):
        self.display.welcome_message()
        board_size = self.menu.board_size_selection(self.board_option)
        player_game_selection = self.menu.player_game_selection(
            self.player_game_options)

        board = self.prepare_board(board_size)
        player_1, player_2 = self.prepare_players(player_game_selection, board)

        game = Game(board=board, display=self.display,
                    game_logic=self.game_logic, player_1=player_1, player_2=player_2)

        return game

    def __prepare_human_players(self, board):
        player_1 = HumanPlayer(name="Player 1", symbol="X", board=board,
                                    display=self.display, input_validator=self.input_validator)

        player_2 = HumanPlayer(name="Player 2", symbol="O", board=board,
                                    display=self.display, input_validator=self.input_validator)

        return [player_1, player_2]

    def __prepare_human_and_easy_computer_players(self, board):
        player_1 = HumanPlayer(name="Player 1", symbol="X", board=board,
                                    display=self.display, input_validator=self.input_validator)

        player_2 = EasyComputerPlayer(
            name="Easy Computer", symbol="O", board=board)

        return [player_1, player_2]

    def __prepare_human_and_medium_computer_players(self, board):
        player_1 = HumanPlayer(name="Player 1", symbol="X", board=board,
                                    display=self.display, input_validator=self.input_validator)

        medium_computer_opponent = player_1.symbol

        player_2 = MediumComputerPlayer(
            name="Medium Computer", symbol="O", board=board, opponent_symbol=medium_computer_opponent)

        return [player_1, player_2]

    def __prepare_human_and_hard_computer_players(self, board):
        player_1 = HumanPlayer(name="Player 1", symbol="X", board=board,
                                    display=self.display, input_validator=self.input_validator)

        hard_computer_opponent = self.player_1.symbol

        player_2 = HardComputerPlayer(
            name="Hard Computer", symbol="O", board=board, opponent_symbol=hard_computer_opponent, game_logic=self.game_logic)

        return [player_1, player_2]
