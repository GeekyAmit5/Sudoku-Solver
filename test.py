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







import pygame
import sys


pygame.init()
win_width = 1000
win_height = 600
win = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption("Sudoku")
Clock = pygame.time.Clock()
fps = 60
black = (0, 0, 0)
white = (255, 255, 255)
green = (51, 204, 89)
red = (250, 51, 51)


#creating cell class that represent every square in sudoku
class cell:
    def __init__(self,(i,j),rect,color,border,border_color,num,num_color):
        self.id = (i,j)
        self.rect = rect
        self.color = color
        self.border = border
        self.border_color = border_color
        self.num = num
        self.num_color = num_color
        self.isActive = False
        self.isPermanant = self.num != 0


    def show(self):
        pygame.draw.rect(win,self.color,self.rect)
        pygame.draw.rect(win,self.border_color,self.rect,self.border)
        if self.num:
            win.blit(num_font.render(str(self.num),True,self.num_color), (self.rect.x+20,self.rect.y+15))


#grid attributes
grid_side_margin = 100
grid_top_margin = 30
cell_size = 60
cell_border = 2
cell_border_color = black
cell_color = white
cell_num_color = black
cell_num = 0
num_font = pygame.font.SysFont(None,40)
grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]


cells = []
for i in range(9):
    for j in range(9):
        object = cell((i,j),pygame.Rect(grid_side_margin+j*cell_size,grid_top_margin+i*cell_size,cell_size,cell_size),cell_color,cell_border,cell_border_color,grid[i][j],cell_num_color)
        cells.append(object)


def isPossible(id, n):
    for i in range(9):
        if cell.id[0]
        if grid[x][i] == n or grid[i][y] == n:
            return False
    for i in range(3):
        for j in range(3):
            if grid[(x//3)*3+i][(y//3)*3+j] == n:
                return False
    return True


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for cell in cells:
                    if cell.rect.collidepoint(event.pos):
                        cell.isActive = True
                    else:
                        cell.isActive = False
            if event.type == pygame.KEYDOWN:
                for cell in cells:
                    if cell.isActive and not cell.isPermanant:
                        if event.key == pygame.K_BACKSPACE:
                            cell.num = 0
                        else:
                            cell.num = int(event.unicode)
                            

        win.fill(white)
        for cell in cells:
            cell.show()
        Clock.tick(fps)
        pygame.display.update()


main()
