import Piece, Move

class Board(object):
    """Manipulates the chess board"""
    def __init__(self):
        """Calls create_board method to make the initialize the board when Board is instantiated"""
        self.main_board = []
        Move.set_new_game(self.main_board)

