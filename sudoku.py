import time
import pygame
import numpy as np

pygame.init()
width = 500
height = 500
row = 9
column = 9
pygame.display.set_caption("Sudoku")
win = pygame.display.set_mode((width, height))
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# easy
grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]


# expert
# grid = [[2, 0, 0, 0, 0, 0, 5, 0, 0],
#         [8, 0, 0, 0, 6, 0, 2, 0, 0],
#         [0, 0, 0, 0, 0, 8, 0, 7, 0],
#         [0, 0, 9, 0, 0, 7, 0, 0, 0],
#         [0, 0, 0, 9, 0, 0, 8, 0, 0],
#         [0, 0, 1, 0, 0, 5, 0, 0, 7],
#         [0, 0, 0, 0, 1, 0, 0, 0, 6],
#         [0, 2, 0, 7, 0, 0, 0, 4, 0],
#         [0, 5, 0, 6, 0, 0, 0, 1, 0]]


# generate a sudoku
# grid=[[0 for x in range(9)]for y in range(9)]
total = 0


def isPossible(x, y, n):
    for i in range(9):
        if grid[x][i] == n or grid[i][y] == n:
            return False
    for i in range(3):
        for j in range(3):
            if grid[(x//3)*3+i][(y//3)*3+j] == n:
                return False
    return True


def writeIt(color, x, y, n):
    r = 3 * row
    c = 3 * column
    x = 3 * x+1
    y = 3 * y+1
    score = pygame.font.Font(
        'freesansbold.ttf', 20).render(str(n), True, color)
    win.blit(score, (y * width / c+3, x * height / r))


def colorIt(color, x, y):
    # pygame.time.delay(5)
    pygame.draw.rect(win, color, (3 + y * width / column, 3 + x *
                                  height / row, width / column - 3, height / row - 3))


def solve():
    global grid, total
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for n in range(1, 10):
                    if isPossible(i, j, n):
                        grid[i][j] = n
                        colorIt(green, i, j)
                        writeIt(black, i, j, grid[i][j])
                        pygame.display.update()
                        solve()
                        grid[i][j] = 0
                        colorIt(red, i, j)
                        pygame.display.update()
                return
    print(np.matrix(grid), "\n")
    total += 1
    print("Total :", total)
    # time.sleep(3)
    # exit()


def drawGrid(color, row, column):
    for i in range(1, column):
        if not i % 3:
            pygame.draw.line(win, color,
                             (i * width / column, 0), (i * width / column, height), 4)
        else:
            pygame.draw.line(win, color,
                             (i * width / column, 0), (i * width / column, height), 2)
    for i in range(1, row):
        if not i % 3:
            pygame.draw.line(win, color,
                             (0, i * height / row), (width, i * height / row), 4)
        else:
            pygame.draw.line(win, color,
                             (0, i * height / row), (width, i * height / row), 2)


def main():
    win.fill(white)
    drawGrid(black, row, column)
    for i in range(9):
        for j in range(9):
            if grid[i][j]:
                writeIt(blue, i, j, grid[i][j])
    pygame.display.update()


main()
solve()
