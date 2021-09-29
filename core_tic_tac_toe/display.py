class Display:
    def render(self, moves):
        print("    |    |    ")
        print(" {}  | {}  | {} ".format(moves[0], moves[1], moves[2]))
        print("    |    |    ")
        print("--------------")
        print("    |    |    ")
        print(" {}  | {}  | {} ".format(moves[3], moves[4], moves[5]))
        print("    |    |    ")
        print("--------------")
        print("    |    |    ")
        print(" {}  | {}  | {} ".format(moves[6], moves[7], moves[8]))
        print("    |    |    ")
