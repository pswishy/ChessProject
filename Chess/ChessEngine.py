"""
this class is responsible for determing the valid moves a player can make at any point during the game.
It will also keep a log of the users move.

"""
class Gamestate():

    def __init__(self):

        """
        initializer creates the 8x8 chess board. '--' represents empty space on the board
        b or w indicates the color of each piece.
        """
        self.board = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        self.moveFunctions = {'p': self.getPawnMoves, "R": self.getRookMoves,
                              'N': self.getKnightMoves, 'B': self.getBishopMoves,
                              'Q': self.getQueenMoves, "K": self.getKingMoves}
        self.whiteToMove = True
        self.moveLog = []
        self.whiteKingPosition = (7, 4)
        self.blackKingPosition = (0, 4)



    def makeMove(self, move):
        """
        takes a move as parameter and exeutes it. does not work for castling
        :param move:
        :return:
        """
        self.board[move.startRow][move.startColumn] = '--'
        self.board[move.endRow][move.endColumn] = move.pieceMoved
        self.moveLog.append(move) # log the user move
        self.whiteToMove = not self.whiteToMove # switch player
        if move.pieceMoved == 'wK':
            self.whiteKingPosition = (move.endRow, move.endColumn)
        elif move.pieceMoved == 'bK':
            self.blackKingPosition = (move.endRow, move.endColumn)



    def undoMove(self):
        if len(self.moveLog) != 0: # edgecase to make sure a move has been made
            move = self.moveLog.pop()
            self.board[move.startRow][move.startColumn] = move.pieceMoved
            self.board[move.endRow][move.endColumn] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove
            if move.pieceMoved == 'wK':
                self.whiteKingPosition = (move.startRow, move.startColumn)
            elif move.pieceMoved == 'bK':
                self.blackKingPosition = (move.startRow, move.startColumn)

            #piece = move.pieceMoved
            #move = move.getChessNotation()
            #undo_move = move[6:] + move[2:6] + move[0:2]
            #print("*UNDO*" + " " + piece + " " + undo_move)

    def ValidMoves(self):
        """
        generates all possible moves for a piece by calling allPossibleMoves()
        make the move then generate all possible opponets moves. check to see if
        opponents move attacks king and if they do it is not a valid move
        """
        #return self.allPossibleMoves()
        moves = self.allPossibleMoves()
        for i in range(len(moves)-1 , -1, -1):

            self.makeMove(moves[i])
            self.whiteToMove = not self.whiteToMove
            if self.inCheck():
                moves.remove(moves[i])
        # #
            self.whiteToMove = not  self.whiteToMove
            self.undoMove()

        return moves





    def inCheck(self):
        """
        determines if user is in check
        :return: boolean that says if user in check
        """
        if self.whiteToMove:
            return self.squareUnderAttack(self.whiteKingPosition[0], self.whiteKingPosition[1])
        else:
            return self.squareUnderAttack(self.blackKingPosition[0], self.blackKingPosition[1])

    def squareUnderAttack(self, row, column):
        """

        :param row: row of king in check
        :param column: column of king in check
        :return:
        """
        self.whiteToMove = not self.whiteToMove
        oppmoves = self.allPossibleMoves()
        self.whiteToMove = not self.whiteToMove
        for move in oppmoves:
            if move.endRow == row and move.endColumn == column:
                return True
        return False


    def allPossibleMoves(self):

        moves = []
        for row in range(len(self.board)):
            for column in range(len(self.board)):
                player_turn = self.board[row][column][0]
                if (player_turn == 'w' and self.whiteToMove) or (player_turn == 'b' and not self.whiteToMove):
                    piece = self.board[row][column][1]
                    self.moveFunctions[piece](row, column, moves)

        return moves


    def getPawnMoves(self, row, column, moves):
        """
        logic for how a pawn moves
        :param row:
        :param column:
        :param moves:
        :return:
        """
        if self.whiteToMove: # white pawn moving
            if self.board[row - 1][column] == '--': # pawn moving one square forward
                moves.append(Move((row, column), (row - 1, column), self.board))
                if row == 6 and self.board[row - 2][column] == '--': # white pawn moving two squares forward on first turn
                    moves.append(Move((row, column), (row - 2, column), self.board))
            if column - 1 >= 0: # captures to the left
                if self.board[row - 1][column - 1][0] == 'b':
                    moves.append(Move((row, column), (row - 1, column-1), self.board))
            if column + 1 <=7:
                if self.board[row - 1][column + 1][0] == 'b':
                    moves.append(Move((row, column), (row - 1, column+1), self.board))

        else: #black pawn moves
            if self.board[row + 1][column] == '--': #black pawn moving one forward
                moves.append(Move((row, column), (row + 1, column), self.board))
                if row == 1 and self.board[row+2][column] == '--': #black pawn in starting position and wants to mmove two forward
                    moves.append(Move((row, column), (row + 2, column), self.board))
            if column - 1 >= 0: # captures to the left
                if self.board[row + 1][column - 1][0] == 'w':
                    moves.append(Move((row, column), (row + 1, column - 1), self.board))
            if column + 1 <= 7: # captures to left
                if self.board[row + 1][column + 1][0] == 'w':
                    moves.append(Move((row, column), (row + 1, column + 1), self.board))




    def getRookMoves(self, row, column, moves):
        """
        logic for how a rook moves
        :param row:
        :param column:
        :param moves:
        :return:
        """
        diretions = ((-1, 0), (0, -1), (1, 0), (0, 1))
        if self.whiteToMove:
            enemy_color = 'b'
        else:
            enemy_color = 'w'

        for d in diretions:
            for i in range(1, 8):
                endrow = row + d[0] * i
                endcol = column + d[1] * i
                if 0 <= endrow < 8 and 0 <= endcol < 8:
                    endpiece = self.board[endrow][endcol]
                    if endpiece == '--': # empty space
                        moves.append(Move((row, column), (endrow, endcol), self.board))

                    elif endpiece[0] == enemy_color: #capture opponent piece
                        moves.append(Move((row, column), (endrow, endcol), self.board))

                    else: # friendly piece reached
                        break
                else:
                    break



    def getBishopMoves(self, row, column, moves):
        """
        logic for how a bishop moves
        :param row:
        :param column:
        :param moves:
        :return:
        """
        diretions = ((-1, -1), (-1, 1), (1, -1), (1, 1))
        if self.whiteToMove:
            enemy_color = 'b'
        else:
            enemy_color = 'w'

        for d in diretions:
            for i in range(1, 8):
                endrow = row + d[0] * i
                endcol = column + d[1] * i
                if 0 <= endrow < 8 and 0 <= endcol < 8:
                    endpiece = self.board[endrow][endcol]
                    if endpiece == '--':  # empty space
                        moves.append(Move((row, column), (endrow, endcol), self.board))

                    elif endpiece[0] == enemy_color:  # capture opponent piece
                        moves.append(Move((row, column), (endrow, endcol), self.board))

                    else:  # friendly piece reached
                        break
                else:
                    break

    def getKnightMoves(self, row, column, moves):
        """
        logic for how a knight will move
        :param row:
        :param column:
        :param moves:
        :return:
        """
        diretions = ((-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))
        if self.whiteToMove:
            enemy_color = 'b'
        else:
            enemy_color = 'w'

        for d in diretions:
            for i in range(1, 8):
                endrow = row + d[0]
                endcol = column + d[1]
                if 0 <= endrow < 8 and 0 <= endcol < 8:
                    endpiece = self.board[endrow][endcol]
                    if endpiece == '--':  # empty space
                        moves.append(Move((row, column), (endrow, endcol), self.board))

                    elif endpiece[0] == enemy_color:  # capture opponent piece
                        moves.append(Move((row, column), (endrow, endcol), self.board))

                    else:  # friendly piece reached
                        break
                else:
                    break

    def getQueenMoves(self, row, column, moves):
        """
        logic for how a queen will move
        :param row:
        :param column:
        :param moves:
        :return:
        """
        diretions = ((-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
        if self.whiteToMove:
            enemy_color = 'b'
        else:
            enemy_color = 'w'

        for d in diretions:
            for i in range(1, 8):
                endrow = row + d[0] * i
                endcol = column + d[1] * i
                if 0 <= endrow < 8 and 0 <= endcol < 8:
                    endpiece = self.board[endrow][endcol]
                    if endpiece == '--':  # empty space
                        moves.append(Move((row, column), (endrow, endcol), self.board))

                    elif endpiece[0] == enemy_color:  # capture opponent piece
                        moves.append(Move((row, column), (endrow, endcol), self.board))

                    else:  # friendly piece reached
                        break
                else:
                    break

    def getKingMoves(self, row, column, moves):
        """
        logic for how a king will move
        :param row:
        :param column:
        :param moves:
        :return:
        """
        kingmoves = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        if self.whiteToMove:
            allycolor = 'w'
        else:
            allycolor = 'b'

        for i in range(8):
            endrow = row + kingmoves[i][0]
            endcol = column + kingmoves[i][1]

            if 0 <= endrow < 8 and 0 <= endcol < 8:
                endpiece = self.board[endrow][endcol]
                if endpiece[0] != allycolor:
                    moves.append(Move((row, column), (endrow, endcol), self.board))
class Move():

    # create dictionaries that follow chess notation for row and columns of chess board
    # in chess notation column is called file(letter) and rows are called rank(number)

    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7":1, "8":0}
    rowsToRanks = {value: key for key, value in ranksToRows.items()}
    filesToColumns = {"a": 0, "b": 1, "c": 2, "d": 3,
                      "e": 4, "f": 5, "g": 6, "h": 7}
    columnsToFiles = {value: key for key, value in filesToColumns.items()}



    def __init__(self, startSq, endSq, board):

        self.startRow = startSq[0]
        self.endRow = endSq[0]
        self.startColumn = startSq[1]
        self.endColumn = endSq[1]
        self.pieceMoved = board[self.startRow][self.startColumn]
        self.pieceCaptured = board[self.endRow][self.endColumn]
        self.moveID = self.startRow * 1000 + self.startColumn * 100 + self.endRow * 10 + self.endColumn

    def __eq__(self, other):
        """
        overriding equals operator to check if user is making a valid move
        :param other: Move object
        :return: boolean that determines if user is making a valid move
        """
        if isinstance(other, Move):
            return self.moveID == other.moveID
        return False


    def getChessNotation(self):
        """
        Function that will allow us to see user move in chess notation
        also will be used when storing user move in database

        :return: user move in chess notation
        """
        return (self.columnsToFiles[self.startColumn] + self.rowsToRanks[self.startRow] + "--->" + self.columnsToFiles[self.endColumn] + self.rowsToRanks[self.endRow])




