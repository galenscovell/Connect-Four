
import pygame, random, sys
from card import Card
from pygame.locals import *


# Constant setup
FPS          = 20
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
BACKGROUND = (142,  68, 173)
BOARD_C    = ( 44,  62,  80)
CARD_C     = ( 39, 174,  96)
SELECTED_C = (243, 156,  18)
COLOR_1    = ( 46, 204, 113)
COLOR_2    = (241, 196,  15)
COLOR_3    = ( 52, 152, 219)
COLOR_4    = (231,  76,  60)

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

    def createIcons(self):
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
        pygame.draw.rect(DISPLAY, BOARD_C, [
                X_MARGIN / 2, 
                Y_MARGIN / 2, 
                WINDOW_X - X_MARGIN, 
                WINDOW_Y - Y_MARGIN
            ])
        return board

    def updateBoard(self, board):
        for card in Card.instances:
            if card.mode == 0:
                card.rect = pygame.draw.rect(DISPLAY, CARD_C, [
                        (CELL_MARGIN + CELLSIZE) * card.x + X_MARGIN + (CELL_MARGIN / 2), 
                        (CELL_MARGIN + CELLSIZE) * card.y + Y_MARGIN + (CELL_MARGIN / 2), 
                        CELLSIZE, CELLSIZE
                    ])
            elif card.mode == 1:
                card.rect = pygame.draw.rect(DISPLAY, card.highlight, [
                        (CELL_MARGIN + CELLSIZE) * card.x + X_MARGIN + (CELL_MARGIN / 2), 
                        (CELL_MARGIN + CELLSIZE) * card.y + Y_MARGIN + (CELL_MARGIN / 2), 
                        CELLSIZE, CELLSIZE
                    ])
            elif card.mode == 2:
                card.rect = pygame.draw.rect(DISPLAY, SELECTED_C, [
                        (CELL_MARGIN + CELLSIZE) * card.x + X_MARGIN + (CELL_MARGIN / 2), 
                        (CELL_MARGIN + CELLSIZE) * card.y + Y_MARGIN + (CELL_MARGIN / 2), 
                        CELLSIZE, CELLSIZE
                    ])

    def guessCard(self, card, first_guess):
        card.mode = 2
        print(first_guess.icon, first_guess.color, card.icon, card.color)
        if card == first_guess:
            pass
        elif card.icon == first_guess.icon and card.color == first_guess.color:
            print("Correct")
        card.mode = 0
        first_guess.mode = 0



def main():
    fpsClock = pygame.time.Clock()

    creating_board = True
    while creating_board:
        DISPLAY.fill(BACKGROUND)
        game = Game()
        icons = game.createIcons()
        board = game.createBoard(icons)
        game.updateBoard(board)
        creating_board = False

    running = True
    first_selected = False
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
                        if first_selected:
                            first_selected = False
                            game.guessCard(card, first_guess)
                        else:
                            card.mode = 2
                            first_guess = card
                            first_selected = True


        game.updateBoard(board)
        pygame.display.flip()
        fpsClock.tick(FPS)

if __name__ == "__main__":
    main()