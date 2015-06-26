class Piece(object):
    """
    Generalized piece class that contains attributes about whether it is an empty piece or if it is black
    or white. All pieces except empty have their own subclass. Contains a list of locations the piece can
    move to.
    """
    def __init__(self):
        self.empty = True
        self.color = "NA"
        self.double_step = False

    def __repr__(self):
        if self.empty:
            return u"\u25A1"
    def move_set(self, piece, board):
        print "Error: This is an empty space"

    def piece_at(self, at, color = None, en_passant = None):
        """
        If only at argument is filled, the function checks to see if there is a chess piece at the given
        coordinate.

        If the color argument is given as well, the function checks to see if the given piece matches
        the queried color.

        If the en passant argument is filled with the piece rank, the function checks if the target piece
        moved two forward initially and whether the attacking piece is on the right rank.
        """
        if color == None:
            if not at.empty:
                return True
            else:
                return False

        elif en_passant == None:   # If color is given but en passant is not
            if at.color == color:
                return True
            else:
                return False

        else:  # En passant
            if at.double_step and at.color == color:
                if at.color == "White" and en_passant == 3:
                    return True
                elif at.color == "Black" and en_passant == 4:
                    return True
                else:
                    return False
            else:
                return False

    def linear_set(self, piece, board, array, direction = None):
        """
        Checks pieces in array until it hits an ally piece or the end of the board.
        Returns the set of valid moves. Direction determines the value of the axis that is to remain
        constant, eg. to check horizontal moves of a rook, the rank remains constant.
        """
        lin_set = []
        piece_ob = board[piece[0]][piece[1]]

        for i in array:
            if direction == 'H':
                coor = (piece[0], i)
                target = board[piece[0]][i]
            elif direction == 'V':
                coor = (i, piece[1])
                target = board[i][piece[1]]
            elif direction == 'D':
                coor = (i[0], i[1])
                target = board[i[0]][i[1]]
            if self.piece_at(target):
                if direction != 'C':   # C is for castling purposes
                    if target.color != piece_ob.color and not target.empty:
                        lin_set.append(coor)
                else:
                    if isinstance(target, Rook) and target.color == self.color:   # If rook on same team
                        lin_set.append(coor)
                break
            else:
                lin_set.append(coor)

        return lin_set

    def standard_set(self, piece, board, displacement):
        """Calculates valid moves given a list of displacement tuples"""
        std_set = []
        piece_ob = board[piece[0]][piece[1]]

        for i in displacement:
            try:
                coor = (piece[0] + i[0], piece[1] + i[1])
                target = board[coor[0]][coor[1]]
                if not self.piece_at(target) or (target.color != piece_ob.color and not target.empty):
                    if coor[0] >= 0 and coor[1] >= 0:   # negative numbers cause weirdness
                        std_set.append(coor)

            except IndexError:
                pass

        return std_set

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

    def move_set(self, piece, board):
        """Consolidates all the movement set information and returns final list of valid moves"""
        total = []
        total.extend(self.standard_moves(piece, board))
        total.extend(self.capture_moves(piece, board))

        return total

    def standard_moves(self, piece, board):
        """
        Takes piece and calculates all the legal spaces the piece can move to, NOT including spaces
        where a piece can be captured. Has branches depending on whether the moving piece is white or
        black.
        """
        self.total = []
        if self.color == "White":
            if not self.piece_at(board[piece[0]][piece[1] + 1]):  # If there is not a piece there
                self.total.append((piece[0], piece[1] + 1))  # One square forward

            if not self.moved and not self.piece_at(board[piece[0]][piece[1] + 2]):
                self.total.append((piece[0], piece[1] + 2))  # Two squares forward

        else:   # If piece is black, the math is backwards
            if not self.piece_at(board[piece[0]][piece[1] - 1]):
                self.total.append((piece[0], piece[1] - 1))

            if not self.moved and not self.piece_at(board[piece[0]][piece[1] - 2]):
                self.total.append((piece[0], piece[1] - 2))

        return self.total

    def capture_moves(self, piece, board):
        """Creates a list of moves where a piece can be captured by the pawn, includes en passant."""
        self.cset = []
        if self.color == "White":
            if self.piece_at(board[piece[0] - 1][piece[1] + 1], "Black"):  # Regular capture
                self.cset.append((piece[0] - 1 , piece[1] + 1))
            if self.piece_at(board[piece[0] + 1][piece[1] + 1], "Black"):
                self.cset.append((piece[0] + 1 , piece[1] + 1))

            if self.piece_at(board[piece[0] - 1][piece[1]], "Black", piece[1]):  # En passant
                self.cset.append((piece[0] - 1, piece[1] + 1))
            if self.piece_at(board[piece[0] + 1][piece[1]], "Black", piece[1]):
                self.cset.append((piece[0] + 1, piece[1] + 1))

        else:
            if self.piece_at(board[piece[0] - 1][piece[1] - 1], "White"):  # Regular capture
                self.cset.append((piece[0] - 1 , piece[1] - 1))
            if self.piece_at(board[piece[0] + 1][piece[1] - 1], "White"):
                self.cset.append((piece[0] + 1 , piece[1] - 1))

            if self.piece_at(board[piece[0] - 1][piece[1]], "White", piece[1]):  # En passant
                self.cset.append((piece[0] - 1, piece[1] - 1))
            if self.piece_at(board[piece[0] + 1][piece[1]], "White", piece[1]):
                self.cset.append((piece[0] + 1, piece[1] - 1))

        return self.cset

class Rook(Piece):
    """Contains attributes of a rook"""
    def __init__(self, empty, color):
        self.empty = empty
        self.color = color
        self.moved = False   # For castling

    def __repr__(self):
        if self.color == "White":
            return u"\u265C"

        else:
            return u"\u2656"

    def move_set(self, piece, board):
        """Consolidates all the movement set information and returns final list of valid moves"""
        total = self.axial_set(piece, board)
        return total

    def axial_set(self, piece, board):
        """Returns moves that are legal and are vertical and horizontal to the piece"""
        axial = []
        axial.extend(self.horizontal_set(piece, board))
        axial.extend(self.vertical_set(piece, board))
        return axial

    def horizontal_set(self, piece, board):
        """
        Finds set of moves that are to the horizontal. Note: due to the layout of the board in this
        program, horizontal means squares in a rank, ie. A1,A2,etc.
        """
        hor_set = []
        col = range(8)
        left = col[:piece[1]]
        left.reverse()              # Reversed so the loop evaluates the square next to the piece first
        right = col[piece[1] + 1:]

        hor_set.extend(self.linear_set(piece, board, left, 'H'))
        hor_set.extend(self.linear_set(piece, board, right, 'H'))

        return hor_set

    def vertical_set(self, piece, board):
        """
        Finds set of moves that are to the vertical of the piece. Note: due to the layout of the board in
        this program, vertical means squares in a file, ie. A1,B1,etc.
        """
        ver_set = []
        row = range(8)
        upper = row[:piece[0]]
        upper.reverse()
        lower = row[piece[0] + 1:]

        ver_set.extend(self.linear_set(piece, board, upper, 'V'))
        ver_set.extend(self.linear_set(piece, board, lower, 'V'))

        return ver_set

class Knight(Piece):
    """Contains attributes of a knight"""
    displacement = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

    def __init__(self, empty, color):
        self.empty = empty
        self.color = color

    def __repr__(self):
        if self.color == "White":
            return u"\u265E"

        else:
            return u"\u2658"

    def move_set(self, piece, board):
        """Returns complete set of legal moves"""
        total = self.standard_set(piece, board, self.displacement)
        return total

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

    def move_set(self, piece, board):
        """Consolidates all the movement set information and returns final list of valid moves"""
        final = self.diagonal_set(piece, board)
        return final

    def diagonal_set(self, piece, board):
        """Calculates moves from the piece in each diagonal direction until they encounter a piece"""
        diag_set = []

        upper_left = [(piece[0] - x - 1, piece[1] - x - 1) for x in range(min(piece[0], piece[1]))]
        upper_right = [(piece[0] - x - 1, piece[1] + x + 1) for x in range(min(piece[0], 7 - piece[1]))]
        lower_left = [(piece[0] + x + 1, piece[1] - x - 1) for x in range(min(7 - piece[0], piece[1]))]
        lower_right = [(piece[0] + x + 1, piece[1] + x + 1) for x in range(min(7-piece[0], 7-piece[1]))]

        diag_set.extend(self.linear_set(piece, board, upper_left, 'D'))
        diag_set.extend(self.linear_set(piece, board, upper_right, 'D'))
        diag_set.extend(self.linear_set(piece, board, lower_left, 'D'))
        diag_set.extend(self.linear_set(piece, board, lower_right, 'D'))

        return diag_set

class Queen(Rook, Bishop):
    """
    Contains attributes of a queen. Queen inherits from Rook and Bishop because effectively, a queen is
    a combination of the movement of rooks and bishops.
    """
    def __init__(self, empty, color):
        self.empty = empty
        self.color = color

    def __repr__(self):
        if self.color == "White":
            return u"\u265B"

        else:
            return u"\u2655"

    def move_set(self, piece, board):
        """Combines axial_set() from rook and diagonal_set() from bishop."""
        total = []
        total.extend(self.axial_set(piece, board))
        total.extend(self.diagonal_set(piece, board))
        return total

class King(Piece):
    """Contains attributes of a king"""
    displacement = [(0,1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    q_disp = [(-1, 0), (-2, 0), (-3, 0), (-4, 0)]
    k_disp = [(1, 0), (2, 0), (3, 0)]
    def __init__(self, empty, color):
        self.empty = empty
        self.color = color
        self.moved = False   # For castling

    def __repr__(self):
        if self.color == "White":
            return u"\u265A"

        else:
            return u"\u2654"

    def move_set(self, piece, board):
        """Creates the moveset for the king"""
        total = []
        total.extend(self.standard_set(piece, board, self.displacement))
        if not self.moved:
            total.extend(self.castle_set(piece, board))
        return total

    def castle_set(self, piece, board):
        """Checks castling on queen's side"""
        castle = []
        for i in xrange(2):
            if i = 1:
                c_side = self.q_disp
                coor = (piece[0], piece[1] - 4)   # Checks until queen's side rook
            else:
                c_side = self.k_disp
                coor = (piece[0], piece[1] + 3)   # Checks until king's side rook

            test = self.linear_set(piece, board, c_side, 'C')

            if coor in test and not board[coor[0]][coor[1]].moved:
                castle.extend(test)   # Extend not append since linear_set returns an array

       return castle
