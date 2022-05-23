from random import randrange


def is_game_over(board):

    diagonals = get_board_diagonals(board.matrix)
    cols = get_board_columns(board.matrix)
    rows = get_board_rows(board.matrix)

    all_directions = diagonals
    all_directions.extend(cols)
    all_directions.extend(rows)

    chars = ['x', 'o']
    for i in all_directions:
        contains = contains_same_char(i, chars[0])
        if contains == True:
            return True

    for i in all_directions:
        contains = contains_same_char(i, chars[1])
        if contains == True:
            return True

    return False


def contains_same_char(arr, char):
    for i in range(len(arr)):
        if char != arr[i]:
            return False
    return True


def get_board_diagonals(matrix):
    desc_diagonal = []
    asc_diagonal = []

    for i in range(len(matrix)):
        desc_diagonal.append(matrix[i][i])
        asc_diagonal.append(matrix[i][len(matrix) - i - 1])

    return [desc_diagonal, asc_diagonal]


def get_board_columns(matrix):
    columns = []
    for i in range(len(matrix)):
        column = []
        for j in range(len(matrix)):
            column.append(matrix[j][i])
        columns.append(column)

    return columns


def get_board_rows(matrix):
    columns = []
    for i in range(len(matrix)):
        column = []
        for j in range(len(matrix)):
            column.append(matrix[i][j])
        columns.append(column)

    return columns


# arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# diagonals = get_board_diagonals(arr)
# cols = get_board_columns(arr)
# rows = get_board_rows(arr)

# all_directions = diagonals
# all_directions.extend(cols)
# all_directions.extend(rows)


def ai_move(board):
    x = randrange(board.dimension)
    y = randrange(board.dimension)
    return x, y
