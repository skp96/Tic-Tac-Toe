class Menu:

    def __init__(self, display, input_validator):
        self.display = display
        self.input_validator = input_validator

    def player_game_options(self, player_game_options):
        all_player_options = (
            f'Please select from the following options:\n' + player_game_options)

        self.display.game_options(all_player_options)

    def player_game_selection(self, player_game_options):
        self.player_game_options(player_game_options)

        player_choice = self.display.get_player_input()

        if self.input_validator.is_game_option_valid(player_choice):
            return player_choice
        else:
            self.display.print_invalid_game_selection_message()
            return self.player_game_selection(player_choice)

    def board_size_selection(self, board_option):
        self.board_option(board_option)

        board_size = self.display.get_player_input()

        if self.input_validator.is_board_size_valid(board_size):
            return board_size
        else:
            self.display.print_invalid_game_selection_message()
            return self.board_size_selection(board_option)

    def board_option(self, board_option):
        self.display.game_options(board_option)
