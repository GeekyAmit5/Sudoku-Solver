import pygame
import sys


pygame.init()
win_width = 1000
win_height = 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Sudoku")
Clock = pygame.time.Clock()
fps = 60
black = (0, 0, 0)
white = (255, 255, 255)
green = (51, 204, 89)
red = (250, 51, 51)


# creating cell class that represent every square in sudoku
class cell:
    def __init__(self, id, rect, color, border, border_color, num, num_color):
        self.id = id
        self.rect = rect
        self.color = color
        self.border = border
        self.border_color = border_color
        self.num = num
        self.num_color = num_color
        self.isActive = False
        self.isPermanant = self.num != 0

    def show(self):
        pygame.draw.rect(win, self.color, self.rect)
        pygame.draw.rect(win, self.border_color, self.rect, self.border)
        if self.num:
            win.blit(num_font.render(str(self.num), True,
                                     self.num_color), (self.rect.x+20, self.rect.y+15))


# grid attributes
grid_side_margin = 100
grid_top_margin = 30
cell_size = 60
cell_border = 2
cell_border_color = black
cell_color = white
cell_num_color = black
cell_num = 0
num_font = pygame.font.SysFont(None, 40)
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
        object = cell((i, j), pygame.Rect(grid_side_margin+j*cell_size, grid_top_margin+i*cell_size,
                                          cell_size, cell_size), cell_color, cell_border, cell_border_color, grid[i][j], cell_num_color)
        cells.append(object)


def isPossible(id, n):
    x = id[0]//3
    y = id[1]//3
    for cell in cells:
        if cell.id == id:
            continue
        elif (cell.id[0] == id[0] or cell.id[1] == id[1]):
            if cell.num == n:
                return False
        elif cell.id[0]//3 == x and cell.id[1]//3 == y:
            if cell.num == n:
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
                            if isPossible(cell.id, cell.num):
                                cell.color = green
                            else:
                                cell.color = red

        win.fill(white)
        for cell in cells:
            cell.show()
        Clock.tick(fps)
        pygame.display.update()


main()
