from ChessEngine import Gamestate, Move
import ChessMain
import unittest, pygame


class test_main(unittest.TestCase):
    """ test to make sure all images are loaded correctly,
        checks if values in image dictionary are of type pygame.Surface """
    def test_load_images(self):
            images = ChessMain.loadImages()
            #print(images)
            # test for loading in pawn images
            self.assertIsInstance(images['wp'], pygame.Surface)
            self.assertIsInstance(images['bp'], pygame.Surface)
            # test for loading in rook images
            self.assertIsInstance(images['wR'], pygame.Surface)
            self.assertIsInstance(images['bR'], pygame.Surface)
            # test for loading in knight images
            self.assertIsInstance(images['wN'], pygame.Surface)
            self.assertIsInstance(images['bN'], pygame.Surface)
            # test for loading in bishop images
            self.assertIsInstance(images['wB'], pygame.Surface)
            self.assertIsInstance(images['bB'], pygame.Surface)
            # test for loading in queen images
            self.assertIsInstance(images['wQ'], pygame.Surface)
            self.assertIsInstance(images['bQ'], pygame.Surface)
            # test for loading in king images
            self.assertIsInstance(images['wK'], pygame.Surface)
            self.assertIsInstance(images['bK'], pygame.Surface)

    def test_getChessNotation(self):

        """test to make sure proper chess notation is displayed when a user makes a move"""

        # white pawn first move
        move_one = Move((6, 0), (4, 0), test_game.board)
        self.assertEqual(move_one.getChessNotation(), 'a2--->a4')

        # black pawn second move
        move_two = Move((1, 4), (3, 4), test_game.board)
        self.assertEqual(move_two.getChessNotation(), 'e7--->e5')

        # same white pawn moves again. test to see if same piece can be moved twice
        move_three = Move((4, 0), (3, 0), test_game.board)
        self.assertEqual(move_three.getChessNotation(), 'a4--->a5')

        # test special piece i.e black knight to see if its notation is correct
        move_four = Move((0, 1), (2, 0), test_game.board)
        self.assertEqual(move_four.getChessNotation(), 'b8--->a6')

        # test special piece i.e white knight to see if its notation is correct
        move_five = Move((7, 7), (3, 7), test_game.board)
        self.assertEqual(move_five.getChessNotation(), 'h1--->h5')


    def test_user_make_valid_move_white(self):

        """
        checks to see if user is attempting a valid chess move.
        when a user clicks a square the chess engine first determines
        what piece the user is selecting then generates a list of valid moves
        depending on the piece selected and the state of the board.

        the user_clicks moves is then compared to all the potential moves that can be made
        depending on the piece the user is trying to make and the state of the board

        if the users move is in the list of valid moves then the move is executed.

        """
        valid_moves = test_game.ValidMoves()
        # test to see if moving a white pawn two spaces forward from the starting board
        # position is a valid move

        move_one = Move((6, 0), (4, 0), test_game.board)
        self.assertIn(move_one, valid_moves)

        # test to see if moving a white knight pawn from the starting board
        # position is not a valid move.
        move_two = Move((7, 1), (5, 0), test_game.board)
        self.assertIn(move_two, valid_moves)

        # test to see if moving a white rook from the starting position is
        # a valid move. This is not a valid move because when the game first starts
        # a rook can not be the first piece to move
        move_three = Move((7, 0), (5, 0), test_game.board)
        self.assertNotIn(move_three, valid_moves)

        # test to see if moving a white queen from the starting position is
        # a valid move. This is not a valid move because when the game first starts
        # a queen can not be the first piece to move
        move_four = Move((7, 3), (5, 0), test_game.board)
        self.assertNotIn(move_four, valid_moves)

        # although b8--->a6 is a valid chess move it should not be in our
        # valid move list because it is not Blacks turn to move. So no Black
        # moves are considered valid
        move_five = Move((0, 1), (2, 0), test_game.board)
        self.assertNotIn(move_five, valid_moves)


    def test_user_make_valid_move_black(self):
        """
        checks to see if user is attempting a valid chess move.
        when a user clicks a square the chess engine first determines
        what piece the user is selecting then generates a list of valid moves
        depending on the piece selected and the state of the board.

        the user_clicks moves is then compared to all the potential moves that can be made
        depending on the piece the user is trying to make and the state of the board

        if the users move is in the list of valid moves then the move is executed.
        """

        second_test_game.whiteToMove = False
        valid_moves = second_test_game.allPossibleMoves()
        # by changing test_game.whiteToMove to false we can generate all the
        # possible moves the Black team can make on the first round

        # check to see if b8--->a6 is a valid chess move on for Black on the first turn
        move_one = Move((0, 1), (2, 0), test_game.board)
        self.assertIn(move_one, valid_moves)

        # check to see if h7---->h6 is a valid chess move for Black on the first turn
        move_two = Move((1, 7), (2, 7), test_game.board)
        self.assertIn(move_two, valid_moves)

        # check to see if f8---->h6 is a valid chess move for Black on the first turn
        move_three = Move((0, 5), (7, 2), test_game.board)
        self.assertNotIn(move_three, valid_moves)

        # check to see if d8--->e4 is a valid chess move for Black on the first turn
        move_four = Move((0, 3), (4, 4), test_game.board)
        self.assertNotIn(move_four, valid_moves)

        # check to see if d7--->d4 is a valid move for Black on the first turn
        move_five = Move((1, 3), (0, 4), test_game.board)
        self.assertNotIn(move_five, valid_moves)


test_game = Gamestate()
second_test_game = Gamestate()
if __name__  == '__main__':

    unittest.main()













