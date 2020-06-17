import time
import numpy as np
import random
import pygame
import sys


class button():
    def __init__(self, rect, color=(0, 0, 0)):
        self.rect = rect
        self.color = color

    def show(self):
        pygame.draw.rect(win, self.color, self.rect)


class text():
    def __init__(self, msg, x, y, color=(255, 255, 255), size=40, font=None):
        self.msg = msg
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.font = font

    def show(self):
        win.blit(pygame.font.Font(self.font, self.size).render(self.msg, True,
                                                               self.color), (self.x, self.y))


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
                        text(str(n), 43+j*62, 40+i*62, black).show()
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
                game(1)


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
                text(str(grid[i][j]), 43+j*62, 40+i*62, black).show()


def game(level):
    global grid
    win.blit(bg, (0, 0))
    for i in range(9):
        for j in range(9):
            grid[i][j] = sudoku[level][i][j]
    load_sudoku()
    for i in range(4):
        button(rect[i]).show()
        text(gamemenu[i], rect[i].x+20, rect[i].y+15).show()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(4):
                    if rect[i].collidepoint(pygame.mouse.get_pos()):
                        if not i:
                            game(level)
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

    button(rect[0]).show()
    text("About", rect[0].x+20, rect[0].y+15).show()
    button(rect[3]).show()
    text("Back", rect[3].x+20, rect[3].y+15).show()

    b1 = button(rect[1])
    t1 = text("Time Limit On", rect[1].x+20, rect[1].y+15)
    if time_limit:
        b1.color = green
        t1.msg = "Time Limit On"
    else:
        b1.color = red
        t1.msg = "Time Limit Off"
    b1.show()
    t1.show()

    b2 = button(rect[2])
    t2 = text("Sound On", rect[2].x+20, rect[2].y+15)
    if sound:
        b2.color = green
        t2.msg = "Sound On"
    else:
        b2.color = red
        t2.msg = "Sound Off"
    b2.show()
    t2.show()

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
                            if not time_limit:
                                b1.color = green
                                t1.msg = "Time Limit On"
                                time_limit = True
                            else:
                                b1.color = red
                                t1.msg = "Time Limit Off"
                                time_limit = False
                        elif i == 2:
                            if not sound:
                                b2.color = green
                                t2.msg = "Sound On"
                                sound = True
                            else:
                                b2.color = red
                                t2.msg = "Sound Off"
                                sound = False
                        elif i == 3:
                            main()
                        b1.show()
                        t1.show()
                        b2.show()
                        t2.show()
        Clock.tick(fps)
        pygame.display.update()


def difficulty():
    win.blit(bg, (0, 0))
    for i in range(4):
        button(rect[i]).show()
        text(difficultymenu[i], rect[i].x+20, rect[i].y+15).show()
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
        button(rect[i]).show()
        text(mainmenu[i], rect[i].x+20, rect[i].y+15).show()
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
gamemenu = ["Reset", "Solution", "New Game", "Main Menu"]
Clock = pygame.time.Clock()
white = (255, 255, 255)
green = (51, 204, 89)
red = (250, 51, 51)
black = (0, 0, 0)
time_limit = True
sound = True
fps = 10


total = 0
s1 = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
      [5, 2, 0, 0, 0, 0, 0, 0, 0],
      [0, 8, 7, 0, 0, 0, 0, 3, 1],
      [0, 0, 3, 0, 1, 0, 0, 8, 0],
      [9, 0, 0, 8, 6, 3, 0, 0, 5],
      [0, 5, 0, 0, 9, 0, 6, 0, 0],
      [1, 3, 0, 0, 0, 0, 2, 5, 0],
      [0, 0, 0, 0, 0, 0, 0, 7, 4],
      [0, 0, 5, 2, 0, 6, 3, 0, 0]]

s2 = [[2, 0, 0, 0, 0, 0, 5, 0, 0],
      [8, 0, 0, 0, 6, 0, 2, 0, 0],
      [0, 0, 0, 0, 0, 8, 0, 7, 0],
      [0, 0, 9, 0, 0, 7, 0, 0, 0],
      [0, 0, 0, 9, 0, 0, 8, 0, 0],
      [0, 0, 1, 0, 0, 5, 0, 0, 7],
      [0, 0, 0, 0, 1, 0, 0, 0, 6],
      [0, 2, 0, 7, 0, 0, 0, 4, 0],
      [0, 5, 0, 6, 0, 0, 0, 1, 0]]


sudoku = [s1, s2]
grid = [[0 for x in range(9)]for y in range(9)]


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