# Classes
* Board
* Pieces
  * Empty
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
137 is the maximum number of moves possible per turn per team



