
import pygame, random, sys
from pygame.locals import *


# Constant setup
WINDOW_X    = 640
WINDOW_Y    = 480
BOARD_X     = 8
BOARD_Y     = 4
CELLSIZE    = 40
CELL_MARGIN = 10
X_MARGIN = int((WINDOW_X - (BOARD_X * (CELLSIZE + CELL_MARGIN))) / 2)
Y_MARGIN = int((WINDOW_Y - (BOARD_Y * (CELLSIZE + CELL_MARGIN))) / 2)

assert (BOARD_X * BOARD_Y) % 2 == 0, "Board must have even number of boxes in order to complete game."

DONUT   = 'donut'
SQUARE  = 'square'
DIAMOND = 'diamond'
OVAL    = 'oval'

# Color setup
BACKGROUND = (142,  68, 173)
BOARD      = ( 44,  62,  80)
CARD       = (236, 240, 241)
COLOR_1    = ( 46, 204, 113)
COLOR_2    = (241, 196,  15)
COLOR_3    = ( 52, 152, 219)
COLOR_4    = (231,  76,  60)

# Constant lists for card selection
SHAPE_LIST = (DONUT, SQUARE, DIAMOND, OVAL)
COLOR_LIST = (COLOR_1, COLOR_2, COLOR_3, COLOR_4)

assert len(SHAPE_LIST) * len(COLOR_LIST) * 2 == (BOARD_X * BOARD_Y), "Board options must match board size."


class Game:
    def createBoard(self):
        icon_list = []
        for color in COLOR_LIST:
            for shape in SHAPE_LIST:
                icon_list.append((shape, color))

        icon_list *= 2
        random.shuffle(icon_list)

        board = []
        for x in range(BOARD_X):
            column = []
            for y in range(BOARD_Y):
                column.append(icon_list[0])
                del icon_list[0]
            board.append(column)
        return board

    def updateBoard(self, board):
        for x in range(BOARD_X):
            for y in range(BOARD_Y):
                print('Nada')


def main():
    # Pygame initial setup
    pygame.init()
    DISPLAY = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
    pygame.display.set_caption('Memory')
    fpsClock = pygame.time.Clock()


    creating_board = True
    while creating_board:
        DISPLAY.fill(BACKGROUND)
        game = Game()
        board = game.createBoard()
        print(board)
        creating_board = False

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        fpsClock.tick(10)

if __name__ == "__main__":
    main()