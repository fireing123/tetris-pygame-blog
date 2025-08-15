import pygame
from data import SHAPES, COLORS, SIZE

# 1, 2, 3, 4...
def draw_block(surface, x, y, color):
    pygame.draw.rect(surface, color, (x*SIZE, y*SIZE, SIZE, SIZE), border_radius=6)

class Block:
    def __init__(self, type, x, y, wall_x, wall_y):
        self.block = self.copy_block(type)
        self.x = x
        self.y = y
        self.type = type
        self.wall_x = wall_x
        self.wall_y = wall_y

    def copy_block(self, type):
        self.type = type
        return [arr.copy() for arr in SHAPES[type]]

    def render(self, surface):
        for i in range(len(self.block)):
            for j in range(len(self.block[i])):
                if self.block[i][j]:
                    draw_block(surface, self.x + j, self.y + i, COLORS[self.type])

class Board:
    def __init__(self, x, y):
        self.board = [[(None, False)] * x for i in range(y)]
    
    def render(self, surface):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                color, value = self.board[i][j]
                if value:
                    draw_block(surface, j, i, COLORS[color])
                    
        end_y = len(self.board[i]) * SIZE
        end_x = len(self.board) * SIZE
        for i in range(len(self.board) + 1):
            pygame.draw.line(surface, (127, 127, 127), (0, i * SIZE), (end_y, i * SIZE))
        for i in range(len(self.board[0]) + 1):
            pygame.draw.line(surface, (127, 127, 127), (i * SIZE, 0), (i * SIZE, end_x))