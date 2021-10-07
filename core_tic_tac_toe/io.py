import os


class Io:
    def get_player_input(self):
        return input()

    def print_message(self, message):
        print(message)

    def clear_console(self):
        os.system("clear")
