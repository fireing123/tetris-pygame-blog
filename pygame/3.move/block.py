import pygame
from data import SHAPES, COLORS, SIZE

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
    
    def rotate_block(self, board):
        # SRS 벽킥 오프셋: [x, y] (중심, 좌, 우, 위, 아래)
        kicks = [
            (0, 0), (1, 0), (-1, 0), (0, -1), (0, 1)
        ]
        # 회전된 블록 생성
        rotated = list(zip(*self.block[::-1]))
        rotated = [list(row) for row in rotated]
        original_x, original_y = self.x, self.y
        original_block = self.block
        for dx, dy in kicks:
            new_x = original_x + dx
            new_y = original_y + dy
            if board.check_block(rotated, new_x, new_y):
                self.block = rotated
                self.x = new_x
                self.y = new_y
                return True  # 회전 성공
        # 모두 실패하면 회전 취소
        self.block = original_block
        self.x = original_x
        self.y = original_y
        return False

    def render(self, surface):
        for i in range(len(self.block)):
            for j in range(len(self.block[i])):
                if self.block[i][j]:
                    draw_block(surface, self.x + j, self.y + i, COLORS[self.type])

class Board:
    def __init__(self, x, y):
        self.board = [[(None, False)] * x for i in range(y)]

    def check_block(self, block, x, y):
        for i in range(len(block)):
            for j in range(len(block[i])):
                if block[i][j]:
                    if 0 > y + i or y + i > len(self.board) - 1:
                        return False
                    if 0 > x + j or x + j > len(self.board[0]) - 1:
                        return False
                    color, value = self.board[y+i][x+j]
                    if value:
                        return False
        return True
    
    def apply_block(self, block, x, y, color):
        for i in range(len(block)):
            for j in range(len(block[i])):
                if block[i][j]:
                    self.board[y+i][x+j] = (color, True)
    
    def render(self, surface):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                color, value = self.board[i][j]
                if value:
                    draw_block(surface, j, i, COLORS[color])
        end_x = len(self.board[i]) * SIZE
        end_y = len(self.board) * SIZE
        for i in range(len(self.board) + 1):
            pygame.draw.line(surface, (127, 127, 127), (0, i * SIZE), (end_x, i * SIZE))
        for i in range(len(self.board[0]) + 1):
            pygame.draw.line(surface, (127, 127, 127), (i * SIZE, 0), (i * SIZE, end_y))
                

class TimerTask:
    """여러번 체크합니다"""
    def __init__(self, tick: int):
        self.tick = tick
        self.last_update = 0
        
    def not_update_run(self):
        if pygame.time.get_ticks() - self.last_update > self.tick:
            return True
        return False

    def run_periodic_task(self):
        if pygame.time.get_ticks() - self.last_update > self.tick:
            self.reset()
            return True
        return False
    
    def reset(self):
        self.last_update = pygame.time.get_ticks()