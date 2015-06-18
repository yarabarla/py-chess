import Piece

def set_new_game(board):
    """Initializes pieces for a new chess game"""
    A, B, C, D, E, F, G, H = [], [], [], [], [], [], [], []
    board.extend([A, B, C, D, E, F, G, H])

    for row in xrange(8):
        for pe in xrange(1,7):
            if pe == 1 or pe == 6:
                board[row][pe] = Pawn()


def test()
    

