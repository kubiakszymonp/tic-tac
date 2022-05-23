class Board:
    def __init__(self, dimension):
        self.dimension = dimension
        self.matrix = [['-' for x in range(dimension)]
                       for y in range(dimension)]

    def draw_board(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                print(self.matrix[i][j], end="")
            print()

    def make_move(self, x, y, player):
        self.matrix[int(x)][int(y)] = "x" if player else "o"
        return self
