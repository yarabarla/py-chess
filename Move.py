from Piece import Piece, Pawn, Rook, Knight, Bishop, Queen, King

class Move(object):
    """Contains all the move methods"""
    def set_new_game(board):
        """
        Initializes pieces for a new chess game.
        Uses two for loops and if/else statements to set the pieces.
        """
        A, B, C, D, E, F, G, H = range(8), range(8), range(8), range(8), range(8), range(8), range(8), range(8) # Feels unpythonic but can't do A = B = C = ... = range(8) since lists are mutable
        board.extend([A, B, C, D, E, F, G, H])

        for row in xrange(8):
            for col in xrange(8):
                if col == 1:
                    board[row][col] = Pawn(False, 'White')

                elif col == 6:
                    board[row][col] = Pawn(False, 'Black')

                elif col in range(2,7):
                    board[row][col] = Piece(True, 'N/A')

                elif col == 0:
                    if row == 0 or row == 7:
                        board[row][col] = Rook(False, 'White')

                    elif row == 1 or row == 6:
                        board[row][col] = Knight(False, 'White')

                    elif row == 2 or row == 5:
                        board[row][col] = Bishop(False, 'White')

                    elif row == 3:
                        board[row][col] = Queen(False, 'White')

                    else:
                        board[row][col] = King(False, 'White')

                else:
                    if row == 0 or row == 7:
                        board[row][col] = Rook(False, 'Black')

                    elif row == 1 or row == 6:
                        board[row][col] = Knight(False, 'Black')

                    elif row == 2 or row == 5:
                        board[row][col] = Bishop(False, 'Black')

                    elif row == 3:
                        board[row][col] = Queen(False, 'Black')

                    else:
                        board[row][col] = King(False, 'Black')


    def get_move():
        """
        Prompts user for desired move. Only using numerical coordinates for now.
        Stores from and to coordinates in tuples. Returns a tuple of these tuples.
        """
        piece_from = tuple(int(i) for i in raw_input("From?"))
        piece_to = tuple(int(i) for i in raw_input("To?"))

        print "Moving from {0} to {1}".format(piece_from, piece_to)
        return (piece_from, piece_to)

    #def move(piece_from, piece_to):
    #    """Rudimentary move function for now"""

