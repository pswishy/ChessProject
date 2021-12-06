import pygame
from Chess import ChessEngine

pygame.init()
WIDTH = 512
HEIGHT = 512

DIMENSION = 8

SQ_SIZE = HEIGHT // DIMENSION

MAX_FPS = 15
IMAGES = {}


def loadImages():
    """
    function that initalizes a global dictionary of images and loads them.
    """
    pieces = ['wp', 'bp', 'wR', 'bR', 'wN', 'bN', 'wQ', 'bQ', 'wK', 'bK','wB','bB']
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load('images/' + piece + ".png"), (SQ_SIZE, SQ_SIZE))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    #screen.fill(pygame.Color("white"))
    game_state = ChessEngine.Gamestate()
    valid_moves = game_state.ValidMoves()
    move_made = False # flag varibale for when a move is made

    loadImages()
    running = True
    square_selcted = () # no square is selected at first. keeps track of the last click of user
    player_clicks = [] # keeps track of player clicks ( two tuples; first click and second click)
    locations = ((343, 409), (9354, 290), (489, 104), (469, 217), (412,413),(412, 300),
    (419, 41), (357, 158), (413, 468), (469, 339), (279, 103), (285, 228), (353, 290), (291, 230),
    (337, 43), (107, 286))

    for i in range(len(locations)):
        move = ChessEngine.Move(locations[i][0], locations[i][1],game_state.board)
        piece = game_state.board[locations[i][0]][locations[i][1]]

        print(piece + " " + move.getChessNotation())

    # while running:
    #     for e in pygame.event.get():
    #         if e.type == pygame.QUIT:
    #             running = False
    #
    #         else:
    #             location = (343, 409)
    #             row = location[0]
    #             col = location[1]
    #
    #             if square_selcted == (row, col): #edge case for if user clicks the same square twice
    #                 square_selcted = ()
    #                 player_clicks = []
    #
    #             else:
    #                 square_selcted = (row, col)
    #                 player_clicks.append(square_selcted)
    #
    #             if len(player_clicks) == 1:
    #                 piece = game_state.board[row][col]
    #
    #             if len(player_clicks) == 2:
    #                 move = ChessEngine.Move(player_clicks[0], player_clicks[1], game_state.board)
    #                 if move in valid_moves:
    #                     game_state.makeMove(move)
    #                     move_made = True
    #                     square_selcted = () # reset user clicks
    #                     player_clicks = []
    #                     print(piece + " " + move.getChessNotation())
    #
    #
    #                 else:
    #                     player_clicks = [square_selcted]


def drawGameState(screen,game_state):

    drawBoard(screen)
    drawPieces(screen, game_state.board)
    """
    displays all graphics in a current game
    :param screen:
    :param game_state: game_state object
    :return:
    """

def drawBoard(screen):
    """
    Draws the squares on the screen. uses a nested for loop to draw columns and rows

    """
    for column in range(DIMENSION):
        for row in range(DIMENSION):
            if (column + row) % 2 == 0:
                pygame.draw.rect(screen, pygame.Color("white"), pygame.Rect(row * SQ_SIZE, column * SQ_SIZE, SQ_SIZE, SQ_SIZE))
            else:
                pygame.draw.rect(screen, pygame.Color("gray"), pygame.Rect(row * SQ_SIZE, column * SQ_SIZE, SQ_SIZE, SQ_SIZE))




def drawPieces(screen, board):
    """
    draws the pieces on the board. Uses
    """

    for column in range(DIMENSION):
        for row in range(DIMENSION):
            piece = board[column][row]
            if piece != '--':
                screen.blit(IMAGES[piece], pygame.Rect(row * SQ_SIZE, column * SQ_SIZE, SQ_SIZE, SQ_SIZE))