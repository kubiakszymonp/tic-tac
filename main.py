from utils.board import Board
from utils.game_over import *

board = Board(3)
player_move = True
while True:
    print("Ruch gracza: ", "Użyszkodnik" if player_move else "Kąkuter")
    try:
        if player_move:
            x, y = input("Enter two values: ").split()
            board = board.make_move(x, y, player_move)
            player_move = not player_move
        else:
            x, y = ai_move(board)
            board = board.make_move(x, y, player_move)
            player_move = not player_move

    except BaseException as ex:
        print(ex)

    board.draw_board()
