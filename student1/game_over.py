def is_game_over(board):
    dim = board.dimension
    char = ""
    # check rows
    for i in range(dim):
        char = board.matrix[i][0]
        for j in range(1, dim):
            checked_char = board.matrix[i][j]
            if checked_char != char:
                break

    return


def contains_same_char(arr):
    char = arr[0]
    for i in range(len(arr)):
        if char != arr[i]:
            return False
    return True


def get_board_diagonals(matrix):
    desc_diagonal = []
    asc_diagonal = []

    for i in range(len(matrix)):
        desc_diagonal.append(matrix[i][i])
        asc_diagonal.append(matrix[i][len(matrix) - i])

    return [desc_diagonal, asc_diagonal]


arr = [[1, 1, 1], [1, 0, 0], [0, 0, 1]]

cont = contains_same_char(arr[1])
a = 4
