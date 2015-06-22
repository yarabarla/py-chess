class Piece(object):
    """
    Generalized piece class that contains attributes about whether it is an empty piece or if it is black or white.
    All pieces except empty have their own subclass. Contains a list of locations the piece can move to
    """
    def __init__(self):
        self.empty = True
        self.color = "NA"

    def __repr__(self):
        if self.empty:
            return u"\u25A1"
    def move_set(self, piece_from, board):
        print "Error: This is an empty space"

class Pawn(Piece):
    """
    Contains attributes of a pawn. Unicode for all black and white pieces switched around since they
    are going to be displayed on a black background
    """
    def __init__(self, empty, color):
        self.empty = empty
        self.color = color
        self.moved = False  # To determine whether the pawn can move two spaces forward
        self.double_step = False  # Used for en passant

    def __repr__(self):
        if self.color == "White":
            return u"\u265f"

        else:
            return u"\u2659"

    def move_set(self, piece_from, board):
        """Consolidates all the movement set information and returns final list"""
        pass

    def generate_moves(self, piece_from, board):
        """Takes piece_from and calculates all the spaces the piece can move to"""
        self.total = []
        if self.color == "White":
            self.total.append((piece_from[0], piece_from[1] + 1))  # One square forward

            if not self.moved:
                self.total.append((piece_from[0], piece_from[1] + 2))  # Two squares forward

        else:   # If piece is black, the math is backwards
            self.total.append((piece_from[0], piece_from[1] - 1))

            if not self.moved:
                self.total.append((piece_from[0], piece_from[1] - 2))

        return self.total

    def capture_set(self, piece_from, board):
        """Creates a list of moves where a piece can be captured by the pawn"""
        self.cset = []
        if self.color == "White":
            if board[piece_from[0] - 1][piece_from[1] + 1].color == "Black":
                self.cset.append((piece_from[0] - 1 , piece_from[1] + 1))
            if board[piece_from[0] + 1][piece_from[1] + 1].color == "Black":
                self.cset.append((piece_from[0] + 1 , piece_from[1] + 1))

        else:
            if board[piece_from[0] - 1][piece_from[1] - 1].color == "White":
                self.cset.append((piece_from[0] - 1 , piece_from[1] - 1))
            if board[piece_from[0] + 1][piece_from[1] - 1].color == "White":
                self.cset.append((piece_from[0] + 1 , piece_from[1] - 1))

        return self.cset


    def piece_at(at, color = None):
        if color == None:
            if not at.empty:
                return True
            else:
                return False

        else:
            if at.color == color:
                return True
            else:
                return False
class Rook(Piece):
    """Contains attributes of a rook"""
    def __init__(self, empty, color):
        self.empty = empty
        self.color = color

    def __repr__(self):
        if self.color == "White":
            return u"\u265C"

        else:
            return u"\u2656"

class Knight(Piece):
    """Contains attributes of a knight"""
    def __init__(self, empty, color):
        self.empty = empty
        self.color = color

    def __repr__(self):
        if self.color == "White":
            return u"\u265E"

        else:
            return u"\u2658"

class Bishop(Piece):
    """Contains attributes of a bishop"""
    def __init__(self, empty, color):
        self.empty = empty
        self.color = color

    def __repr__(self):
        if self.color == "White":
            return u"\u265D"

        else:
            return u"\u2657"

class Queen(Piece):
    """Contains attributes of a queen"""
    def __init__(self, empty, color):
        self.empty = empty
        self.color = color

    def __repr__(self):
        if self.color == "White":
            return u"\u265B"

        else:
            return u"\u2655"

class King(Piece):
    """Contains attributes of a king"""
    def __init__(self, empty, color):
        self.empty = empty
        self.color = color

    def __repr__(self):
        if self.color == "White":
            return u"\u265A"

        else:
            return u"\u2654"


