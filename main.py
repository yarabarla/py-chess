from Board import Board
import Move

game = Board()
print game

while True:
    #game.main_board[2][6].double_step = True
    #game.main_board[1][6].double_step = True
    wanted = game.get_move()
    game.apply_move(wanted[0], wanted[1])
    print game
#print game
#print wanted

