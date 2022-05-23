class Board:
    def __init__(self, dimension):
        self.dimension = dimension
        self.matrix = [['-' for x in range(dimension)]
                       for y in range(dimension)]

    def draw_board(self):
        for i in range(self.dimension):
            print()
