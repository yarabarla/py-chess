from Board import Board
import Move

game = Board()
print game
wanted = game.get_move()
game.move(wanted[0], wanted[1])
print game

