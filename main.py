import time

from utils.board import Board
from utils.game_over import *

board = Board(5)
player_move = True

while True:
    print("Ruch gracza: ", "Użyszkodnik" if player_move else "Kąkuter")
    try:
        if player_move:
            x, y = input("Enter two values: ").split()
            board = board.make_move(x, y, player_move)
            player_move = not player_move
        else:
            x, y = 0, 0
            while not board.can_move(x, y):
                x, y = ai_move(board)
            board = board.make_move(x, y, player_move)
            player_move = not player_move

    except BaseException as ex:
        print(ex)

    win = is_game_over(board)
    if not player_move and win:
        print("Użyszkodnik wygrał")
        board.draw_board()
        break
    elif win:
        print("Kąkuter wygrał")
        board.draw_board()
        break

    board.draw_board()

