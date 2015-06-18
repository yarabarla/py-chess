class Piece(object):
    """Generalized piece class that contains attributes about whether it is an empty piece or if it is black or white. All pieces except empty have their own subclass. Contains a list of locations the piece can move to"""
    def __init__(self, empty, color):
        self.empty = empty
        self.color = color

    
