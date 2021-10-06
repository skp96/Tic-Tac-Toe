class Io:
    def get_player_input(self):
        self.print_message("Enter a value between 1-9")
        return input()

    def print_message(self, message):
        print(message)
