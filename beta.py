import time
import numpy as np
import random
import pygame
import sys


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
            if not grid[i][j]:
                for n in range(1, 10):
                    if isPossible(i, j, n):
                        grid[i][j] = n
                        pygame.draw.rect(
                            win, green, (22+j*62, 22+i*62, 60, 60))
                        score = font.render(str(n), True, black)
                        win.blit(score, (43+j*62, 40+i*62))
                        pygame.display.update()
                        solve()
                        grid[i][j] = 0
                        pygame.draw.rect(
                            win, red, (22+j*62, 22+i*62, 60, 60))
                        pygame.display.update()
                return
    drawGrid(black)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                game(0)


def drawGrid(color):
    s = 20
    e = 580
    d = 62
    n = 10
    for i in range(n):
        if not i % 3:
            w = 5
        else:
            w = 2
        pygame.draw.line(win, color, (s+d*i, s), (s+d*i, e), w)
    for i in range(n):
        if not i % 3:
            w = 5
        else:
            w = 2
        pygame.draw.line(win, color, (s, s+d*i), (e, s+d*i), w)


def reset():
    load_sudoku()


def load_sudoku():
    pygame.draw.rect(win, white, (20, 20, 560, 560))
    drawGrid(black)
    for i in range(9):
        for j in range(9):
            if grid[i][j]:
                score = font.render(str(grid[i][j]), True, black)
                win.blit(score, (43+j*62, 40+i*62))


def game(level):
    win.blit(bg, (0, 0))
    load_sudoku()
    for i in range(4):
        pygame.draw.rect(win, black, rect[i])
        win.blit(font.render(gamemenu[i], True,
                             white), (rect[i].x+20, rect[i].y+15))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(4):
                    if rect[i].collidepoint(pygame.mouse.get_pos()):
                        if not i:
                            reset()
                        elif i == 1:
                            solve()
                        elif i == 2:
                            difficulty()
                        elif i == 3:
                            main()
        Clock.tick(fps)
        pygame.display.update()


def options():
    global sound, time_limit
    win.blit(bg, (0, 0))
    for i in range(4):
        pygame.draw.rect(win, black, rect[i])
        win.blit(font.render(optionsmenu[i], True,
                             white), (rect[i].x+20, rect[i].y+15))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(4):
                    if rect[i].collidepoint(pygame.mouse.get_pos()):
                        if not i:
                            pass
                        elif i == 1:
                            if time_limit:
                                time_limit = False
                                pygame.draw.rect(win, red, rect[i])
                                optionsmenu[1] = "Time Limit Off"
                            else:
                                time_limit = True
                                pygame.draw.rect(win, green, rect[i])
                                optionsmenu[1] = "Time Limit On"
                        elif i == 2:
                            if sound:
                                sound = False
                                pygame.draw.rect(win, red, rect[i])
                                optionsmenu[2] = "Sound Off"
                            else:
                                sound = True
                                pygame.draw.rect(win, green, rect[i])
                                optionsmenu[2] = "Sound On"
                        elif i == 3:
                            main()
        for i in range(4):
            win.blit(font.render(optionsmenu[i], True,
                                 white), (rect[i].x+20, rect[i].y+15))
        Clock.tick(fps)
        pygame.display.update()


def difficulty():
    win.blit(bg, (0, 0))
    for i in range(4):
        pygame.draw.rect(win, black, rect[i])
        win.blit(font.render(difficultymenu[i], True,
                             white), (rect[i].x+20, rect[i].y+15))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(4):
                    if rect[i].collidepoint(pygame.mouse.get_pos()):
                        if i == 3:
                            main()
                        else:
                            game(i)
        Clock.tick(fps)
        pygame.display.update()


def main():
    win.blit(bg, (0, 0))
    for i in range(4):
        pygame.draw.rect(win, black, rect[i])
        win.blit(font.render(mainmenu[i], True,
                             white), (rect[i].x+20, rect[i].y+15))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(4):
                    if rect[i].collidepoint(pygame.mouse.get_pos()):
                        if not i:
                            pass
                        elif i == 1:
                            difficulty()
                        elif i == 2:
                            options()
                        elif i == 3:
                            pygame.quit()
                            sys.exit()
        Clock.tick(fps)
        pygame.display.update()


pygame.init()
win = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Sudoku")
# icon = pygame.image.load("assets/images/icon.ico")
# pygame.display.set_icon(icon)
bg = pygame.image.load("assets/images/bg.jpg")

rect = []
for i in range(4):
    rect.append(pygame.Rect(625, 240+70*i, 300, 60))
mainmenu = ["Continue", "New Game", "Options", "Exit"]
difficultymenu = ["Easy", "Medium", "Hard", "Back"]
optionsmenu = ["About", "Time Limit off", "Sounds on", "Back"]
gamemenu = ["Reset", "Solution", "New Game", "Main Menu"]
font = pygame.font.Font(None, 40)
Clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
green = (51, 204, 89)
red = (250, 51, 51)
fps = 10


total = 0
time_limit = True
sound = True
grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]


main()


# def generateSudoku():
#     global grid
#     for i in range(20):
#         while True:
#             x, y = random.randint(0, 8), random.randint(0, 8)
#             if not grid[x][y]:
#                 while True:
#                     j = random.randint(0, 9)
#                     if isPossible(x, y, j):
#                         grid[x][y] = j
#                         break
#                 break


# def createSudoku():
#     global grid
#     for i in range(50):
#         while True:
#             x, y = random.randint(0, 8), random.randint(0, 8)
#             if grid[x][y]:
#                 grid[x][y] = 0
#                 break
