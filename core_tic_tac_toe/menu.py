class Menu:

    def __init__(self, display, input_validator):
        self.display = display
        self.input_validator = input_validator

    def game_options(self, game_options):
        all_game_options = (
            f'Please select from the following options:\n' + game_options)

        self.display.game_options(all_game_options)

    def game_selection(self, game_options):
        self.game_options(game_options)

        game_option = self.display.get_player_input()

        if self.input_validator.is_game_option_valid(game_option):
            return game_option
        else:
            self.display.print_invalid_game_selection_message()
            return self.game_selection(game_options)
