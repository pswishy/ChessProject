### What We Need

* Python 
* PyGame
* Pictures/images of the chess pieces you want to use for the game.

### First step in Building

###The first thing we will have to do is create our two files
* the first will be our main file which will be responsible for:
    - loading in our images
    - drawing the board
    - drawing the pieces
    - allowing the user to click the chess board and move the desired piece
    - keeping track of the state of the game. i.e updating the board after a piece has been moved
    - allowing the user to undo a move

### the second file we will have to create is our chess engine file 
* this file is responsible for all the logic that has to be implemented to play chess. This includes:
    - Rendering all valid moves a player can make
    - Determining the direction each individual chess piece can make
      - i.e how a pawn moves, rook, queen etc
    - Displaying proper chess notation after a user makes a move
    - Logging each user moves
    - Allowing a user to undo a move after it has been done