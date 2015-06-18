class Piece(object):
    """Generalized piece class that contains attributes about whether it is an empty piece or if it is black or white. All pieces except empty have their own subclass. Contains a list of locations the piece can move to"""
    def __init__(self, empty, color):
        self.empty = empty
        self.color = color

class Pawn(Piece):
    """Contains attributes of a pawn. Unicode for black and white pieces switched around since they are going to be displayed on a black background"""
    def __repr__(self):
        if self.color == "White":
            return u"\u265f"

        else:
            return u"\u2659"

class Rook(Piece):
    """Contains attributes of a rook"""
    pass

class Knight(Piece):
    """Contains attributes of a knight"""
    pass

class Bishop(Piece):
    """Contains attributes of a bishop"""
    pass

class Queen(Piece):
    """Contains attributes of a queen"""
    pass

class King(Piece):
    """Contains attributes of a king"""
    pass


