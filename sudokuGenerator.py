import time
import pygame
import numpy as np


def isPossible(x, y, n):
    for i in range(9):
        if grid[x][i] == n or grid[i][y] == n:
            return False
    for i in range(3):
        for j in range(3):
            if grid[(x//3)*3+i][(y//3)*3+j] == n:
                return False
    return True


def solve():
    global grid, total
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for n in range(1, 10):
                    if isPossible(i, j, n):
                        grid[i][j] = n
                        solve()
                        grid[i][j] = 0
                return
    print(np.matrix(grid), "\n")
    total += 1
    print("Total :", total, "\n")
    if num == total:
        exit()


if __name__ == "__main__":
    num = int(input("How many Sudoku you want? "))
    total = 0
    grid = [[0 for x in range(9)]for y in range(9)]
    solve()
