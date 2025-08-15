import pygame
import random
from collections import deque
from block import Block, Board, TimerTask
from data import INDEX

DISPLAY_SIZE = (680, 800)

pygame.init() # 초기화 pygame 관련 함수 사용시 무조건 선행되어야함
pygame.display.set_caption("Tetris")

title_font = pygame.font.SysFont("malgungothic", 50)
font = pygame.font.SysFont("malgungothic", 30)

title = title_font.render("테트리스", False, (255, 255, 255))

descriptions = [
    font.render(i, False, (255, 255, 255))
    for i in [
        "←; right",
        "→: left",
        "↑: rotate",
        "↓: 빠르게 내려감",
        "space: 하드 드롭"
    ]
]

clock = pygame.Clock()
screen = pygame.display.set_mode(DISPLAY_SIZE)

is_running = True

board = Board(10, 20)

block = Block("I", 2, 2, 10, 20)

down = TimerTask(500)

while is_running:
    clock.tick(60) # FPS 60 초당 60번 렌더링으로 제한

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                block.rotate_block(board)
            elif event.key == pygame.K_RIGHT:
                if board.check_block(block.block, block.x + 1, block.y):
                    block.x += 1
            elif event.key == pygame.K_LEFT:
                if board.check_block(block.block, block.x - 1, block.y):
                    block.x -= 1
            elif event.key == pygame.K_DOWN:
                down.tick = 90
            elif event.key == pygame.K_SPACE:
                y = 1
                while board.check_block(block.block, block.x, block.y + y):
                    y += 1
                down.last_update = 0
                block.y += y - 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                down.tick = 500

    if down.run_periodic_task():
        if board.check_block(block.block, block.x, block.y + 1):
            block.y += 1
        else:
            board.apply_block(block.block, block.x, block.y, block.type)
            type = random.choice(INDEX)
            block.block = block.copy_block(type)
            block.x = 4
            block.y = 0
            if len(board.get_full_rows()) != 0:
                board.remove_rows()

            down.reset()

            if not board.check_block(block.block, block.x, block.y):
                is_running = False
    
    screen.fill((0, 0, 0))

    block.render(screen)
    board.render(screen)

    screen.blit(title, (420, 200))

    for i in range(len(descriptions)):
        screen.blit(descriptions[i], (420, 300 + 50*i))

    pygame.display.update() # 화면에 screen 에 내용을 나타내는 함수
