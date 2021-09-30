class Display:
    def print_board(self, moves):
        horizontal_bar = self.__horizontal_bar()
        vertical_bars = self.__vertical_bars()

        board = (
            vertical_bars +
            "  {}  |  {}  |  {} \n".format(moves[0], moves[1], moves[2]) +
            vertical_bars +
            horizontal_bar +
            vertical_bars +
            "  {}  |  {}  |  {} \n".format(moves[3], moves[4], moves[5]) +
            vertical_bars +
            horizontal_bar +
            vertical_bars +
            "  {}  |  {}  |  {} \n".format(moves[6], moves[7], moves[8]) +
            vertical_bars
        )

        return board

    def __horizontal_bar(self):
        return "-----------------\n"

    def __vertical_bars(self):
        return "     |     |    \n"
