# Classes
* Board
* Pieces 
  * Pawn
  * Rook
  * Knight
  * Bishop
  * Queen
  * King
 

## Board
* Will contain a 2d grid of coordinates using an array of 8 arrays, each containing 8 Piece elements
* Board will be arranged like A = [ R P E E E E P R ]
                              B = [ N P E E E E P K ]
                              C = [ B P E E E E P B ]
                              D = [ Q P E E E E P Q ]
                              E = [ K P E E E E P K ]
                              F = [ B P E E E E P B ]
                              G = [ N P E E E E P N ]
                              H = [ R P E E E E P R ]
  
* Movement will be coordinated at this level

## Pieces
* Attributes
  * Black, White, or Empty
  * List of locations the piece can move to
  



# Movement
*137 is the maximum number of moves possible per turn per team
* Will need a flipped algorithm to calculate forward and backward vectors for black since + movement for white would be - movement relative to how black moves.
* Each piece class will have a legal_move method that encodes the rules of how that piece can move and generates a list of possible move locations. The desired move coordinates are searched for in that list. Returns True if found and False if not.
* When a move is requested, the legal_move method is called on the moving piece.
* Need to figure out en passante rules
* Need to figure out castling rules

# Goals for Tomorrow
* Change get move so user can actually input board coordinates instead of array coordinates --eg. A2 to A4 rather than (0,1) to (0, 3)
* 
