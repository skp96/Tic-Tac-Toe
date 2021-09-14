class Board:
    def __init__(self):
        self.grid = [
            (1,1), (1,2), (1,3),
            (2,1), (2,2), (2,3),
            (3,1), (3,2), (3,3)
        ]

    def retrieve_list_of_moves(self):
        return self.grid