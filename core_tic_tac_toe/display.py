class Display:
    def render(self, moves):
        horizontal_bar = self.__horizontal_bar()
        vertical_bars = self.__vertical_bars()

        print(vertical_bars)
        print(" {}  | {}  | {} ".format(moves[0], moves[1], moves[2]))
        print(vertical_bars)
        print(horizontal_bar)
        print(vertical_bars)
        print(" {}  | {}  | {} ".format(moves[3], moves[4], moves[5]))
        print(vertical_bars)
        print(horizontal_bar)
        print(vertical_bars)
        print(" {}  | {}  | {} ".format(moves[6], moves[7], moves[8]))
        print(vertical_bars)

    def __horizontal_bar(self):
        return "--------------"

    def __vertical_bars(self):
        return "    |    |    "
