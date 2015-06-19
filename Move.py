import Piece

def set_new_game(board):
    """Initializes pieces for a new chess game"""
    A, B, C, D, E, F, G, H = range(8), range(8), range(8), range(8), range(8), range(8), range(8), range(8) # Feels unpythonic but can't do A = B = C = ... = range(8) since lists are mutable
    board.extend([A, B, C, D, E, F, G, H])

    for row in xrange(8):
        for col in xrange(8):  # Columns 1 - 6 are all pawns and empty so this loop is to place them
            if col == 1:
                board[row][col] = Piece.Pawn(False, 'White')

            elif col == 6:
                board[row][col] = Piece.Pawn(False, 'Black')

            elif col in range(2,7):
                board[row][col] = Piece.Piece(True, 'N/A')

            elif col == 0:
                if row == 0 or row == 7:
                    board[row][col] = Piece.Rook(False, 'White')

                elif row == 1 or row == 6:
                    board[row][col] = Piece.Knight(False, 'White')

                elif row == 2 or row == 5:
                    board[row][col] = Piece.Bishop(False, 'White')

                elif row == 3:
                    board[row][col] = Piece.Queen(False, 'White')

                else:
                    board[row][col] = Piece.King(False, 'White')

            else:
                if row == 0 or row == 7:
                    board[row][col] = Piece.Rook(False, 'Black')

                elif row == 1 or row == 6:
                    board[row][col] = Piece.Knight(False, 'Black')

                elif row == 2 or row == 5:
                    board[row][col] = Piece.Bishop(False, 'Black')

                elif row == 3:
                    board[row][col] = Piece.Queen(False, 'Black')

                else:
                    board[row][col] = Piece.King(False, 'Black')

