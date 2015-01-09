
import pygame, random, sys
from card import Card
from pygame.locals import *


# Constant setup
FPS          = 30
WINDOW_X     = 640
WINDOW_Y     = 480
BOARD_X      = 8
BOARD_Y      = 4
CELLSIZE     = 60
CELL_MARGIN  = 10
REVEAL_SPEED = 4
X_MARGIN = int((WINDOW_X - (BOARD_X * (CELLSIZE + CELL_MARGIN))) / 2)
Y_MARGIN = int((WINDOW_Y - (BOARD_Y * (CELLSIZE + CELL_MARGIN))) / 2)

assert (BOARD_X * BOARD_Y) % 2 == 0, "Board must have even number of boxes in order to complete game."

DONUT   = 'donut'
SQUARE  = 'square'
DIAMOND = 'diamond'
OVAL    = 'oval'

# Color setup
BACKGROUND = (142,  68, 173)  # Wisteria Purple
BOARD      = ( 44,  62,  80)  # Midnight Blue
CARDBACK   = ( 39, 174,  96)  # Nephritis Green
HIGHLIGHT  = (236, 240, 241)  # Cloud White
COLOR_1    = (211,  84,   0)  # Pumpkin Orange
COLOR_2    = (241, 196,  15)  # Sunflower Yellow
COLOR_3    = ( 52, 152, 219)  # Peter River Blue
COLOR_4    = (231,  76,  60)  # Alizarin Red

# Constant lists for card selection
SHAPE_LIST = (DONUT, SQUARE, DIAMOND, OVAL)
COLOR_LIST = (COLOR_1, COLOR_2, COLOR_3, COLOR_4)

assert len(SHAPE_LIST) * len(COLOR_LIST) * 2 == (BOARD_X * BOARD_Y), "Board options must match board size."

# Pygame initial setup
pygame.init()
DISPLAY = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
pygame.display.set_caption('Memory')


class Game:
    'Game mechanics and creation'

    def createIconList(self):
        icon_list = []
        for color in COLOR_LIST:
            for shape in SHAPE_LIST:
                icon_list.append((shape, color))

        icon_list *= 2
        random.shuffle(icon_list)
        return icon_list

    def createBoard(self, icons):
        board = []
        for x in range(BOARD_X):
            column = []
            for y in range(BOARD_Y):
                card = Card(x, y, icons)
                column.append(card)
                del icons[0]
            board.append(column)
        pygame.draw.rect(DISPLAY, BOARD, [
                X_MARGIN / 2, 
                Y_MARGIN / 2, 
                WINDOW_X - X_MARGIN, 
                WINDOW_Y - Y_MARGIN
            ])
        return board

    def updateBoard(self, board):
        for card in Card.instances:
            if card.mode == 0:
                self.drawCard(card, CARDBACK)
            elif card.mode == 1:
                self.drawCard(card, HIGHLIGHT)
            elif card.mode == 2:
                self.drawCard(card, card.color)

    def drawCard(self, card, color):
        card.rect = pygame.draw.rect(DISPLAY, color, [
                        (CELL_MARGIN + CELLSIZE) * card.x + X_MARGIN + (CELL_MARGIN / 2), 
                        (CELL_MARGIN + CELLSIZE) * card.y + Y_MARGIN + (CELL_MARGIN / 2), 
                        CELLSIZE, CELLSIZE
                    ])

    def checkGuess(self):
        first = Card.guesses[0]
        second = Card.guesses[1]
        if first != second and first.color == second.color:
            print("Match")
            Card.correct.append(first)
            Card.correct.append(second)
            del Card.guesses[:]
        else:
            print("No match")
            for card in Card.guesses:
                card.mode = 0
            del Card.guesses[:]


def main():
    clock = pygame.time.Clock()

    creating_board = True
    while creating_board:
        DISPLAY.fill(BACKGROUND)
        game = Game()
        icons = game.createIconList()
        board = game.createBoard(icons)
        game.updateBoard(board)
        creating_board = False

    guesses = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mouse_x, mouse_y = event.pos
                for card in Card.instances:
                    if card.mode != 2:
                        if card.rect.collidepoint(mouse_x, mouse_y):
                            card.mode = 1
                        else:
                            card.mode = 0

            elif event.type == MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos
                for card in Card.instances:
                    if card.rect.collidepoint(mouse_x, mouse_y):
                        guesses += 1
                        card.revealCard()

        if guesses == 2:
            game.checkGuess()
            guesses = 0

        game.updateBoard(board)
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()