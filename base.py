
from player import Player
from computer import Computer
import pygame

# Color setup
BACKGROUND = ( 44,  62,  80)
BOARD      = ( 52, 152, 219)
EMPTY      = ( 41, 128, 185)
PLAYER1    = ( 46, 204, 113)
PLAYER2    = (231,  76,  60)

# Window settings
pygame.init()
CELLSIZE     = 69
MARGIN       = 6
HEIGHT       = 6
WIDTH        = 7
BOARD_MARGIN = 35
screen_size  = [595, 520]

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Connect-Four")


class Game:
    'Control of game mechanics'

    rounds = 0

    def __init__(self):
        self.rounds += 1

    def updateBoard(self, grid):
        for y in range(0, HEIGHT):
            for x in range(0, WIDTH):
                if grid[y][x] == 1:
                    color = PLAYER1
                elif grid[y][x] == 2:
                    color = PLAYER2
                else:
                    color = EMPTY
                pygame.draw.ellipse(screen, color, 
                    [(MARGIN + CELLSIZE) * x + BOARD_MARGIN, 
                    (MARGIN + CELLSIZE) * y + BOARD_MARGIN, 
                    CELLSIZE, CELLSIZE])

    def createBoard(self):
        pygame.draw.rect(screen, BOARD, [10, 10, (screen_size[0] - 20), (screen_size[1] - 20)])
        grid = []
        for y in range(0, HEIGHT):
            grid.append([])
            for x in range(0, WIDTH):
                grid[y].append(0)
        return grid


def main():
    clock = pygame.time.Clock()
    game_board = Game()

    board_created = False
    while not board_created:
        screen.fill(BACKGROUND)
        new_board = game_board.createBoard()
        board_created = True

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                None

        game_board.updateBoard(new_board)
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()
    quit()
    



if __name__ == "__main__":
    main()

