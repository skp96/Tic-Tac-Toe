class Display:

    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2

    def render(self):
        moves = self.board.board_grid()

        print("    |    |    ")
        print(" {} | {} | {} ".format(self.__turn_player_into_symbol(moves[0]),
              self.__turn_player_into_symbol(moves[1]), self.__turn_player_into_symbol(moves[2])))
        print("    |    |    ")
        print("--------------")
        print("    |    |    ")
        print(" {} | {} | {} ".format(self.__turn_player_into_symbol(moves[3]),
              self.__turn_player_into_symbol(moves[4]), self.__turn_player_into_symbol(moves[5])))
        print("    |    |    ")
        print("--------------")
        print("    |    |    ")
        print(" {} | {} | {} ".format(self.__turn_player_into_symbol(moves[6]),
              self.__turn_player_into_symbol(moves[7]), self.__turn_player_into_symbol(moves[8])))
        print("    |    |    ")

    def __turn_player_into_symbol(self, value):
        if type(value) == int:
            return value

        if value == self.player_1:
            return "X"
        else:
            return "O"
