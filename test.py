import pygame
import sys


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


def drawGrid(color):
    s = 20
    e = 580
    d = 62
    n = 10
    w = 5
    for i in range(n):
        pygame.draw.line(win, color, (s+d*i, s), (s+d*i, e), w)
    for i in range(n):
        pygame.draw.line(win, color, (s, s+d*i), (e, s+d*i), w)


def load_sudoku():
    pygame.draw.rect(win, white, (20, 20, 560, 560))
    drawGrid(black)
    for i in range(9):
        for j in range(9):
            if grid[i][j]:
                text(str(grid[i][j]), 43+j*62, 40+i*62, black).show()
    pygame.display.update()


def main():
    global grid
    win.fill(black)
    drawGrid(white)
    prevx, prevy = -1, -1
    xcord, ycord = -1, -1
    load_sudoku()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if rect.collidepoint((mx, my)):
                    active = True
                else:
                    active = False
                if active:
                    x = (mx-20)//62
                    y = (my-20)//62
                    xcord = 40+x*62
                    ycord = 40+y*62
                    print(x, y)
                    print(xcord, ycord)
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        grid[x][y] = 0
                        pygame.draw.rect(
                            win, black, (xcord-20, ycord-20, 40, 40))
                    else:
                        if grid[x][y] == 0:
                            grid[x][y] = int(event.unicode)
                            win.blit(font.render(str(grid[x][y]), True, black),
                                     (xcord, ycord))
        Clock.tick(fps)
        pygame.display.update()


pygame.init()
win = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Testing")
Clock = pygame.time.Clock()
white = (255, 255, 255)
green = (51, 204, 89)
red = (250, 51, 51)
black = (0, 0, 0)
fps = 10
font = pygame.font.Font(None, 50)
rect = pygame.Rect(20, 20, 560, 560)
active = False
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
