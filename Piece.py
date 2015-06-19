class Piece(object):
    """Generalized piece class that contains attributes about whether it is an empty piece or if it is black or white. All pieces except empty have their own subclass. Contains a list of locations the piece can move to"""
    def __init__(self, empty, color):
        self.empty = empty
        self.color = color

    def __repr__(self):
        if self.empty:
            return u"\u25A1"

class Pawn(Piece):
    """Contains attributes of a pawn. Unicode for all black and white pieces switched around since they are going to be displayed on a black background"""
    def __repr__(self):
        if self.color == "White":
            return u"\u265f"

        else:
            return u"\u2659"

class Rook(Piece):
    """Contains attributes of a rook"""
    def __repr__(self):
        if self.color == "White":
            return u"\u265C"

        else:
            return u"\u2656"

class Knight(Piece):
    """Contains attributes of a knight"""
    def __repr__(self):
        if self.color == "White":
            return u"\u265E"

        else:
            return u"\u2658"

class Bishop(Piece):
    """Contains attributes of a bishop"""
    def __repr__(self):
        if self.color == "White":
            return u"\u265D"

        else:
            return u"\u2657"

class Queen(Piece):
    """Contains attributes of a queen"""
    def __repr__(self):
        if self.color == "White":
            return u"\u265B"

        else:
            return u"\u2655"

class King(Piece):
    """Contains attributes of a king"""
    def __repr__(self):
        if self.color == "White":
            return u"\u265A"

        else:
            return u"\u2654"


