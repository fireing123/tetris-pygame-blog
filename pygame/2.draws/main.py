import pygame
from block import Block, Board

DISPLAY_SIZE = (680, 800)

pygame.init() # 초기화 pygame 관련 함수 사용시 무조건 선행되어야함
pygame.display.set_caption("Tetris")

clock = pygame.Clock()
screen = pygame.display.set_mode(DISPLAY_SIZE)

is_running = True

board = Board(10, 20)

block = Block("I", 2, 2, 10, 20)

while is_running:
    clock.tick(60) # FPS 60 초당 60번 렌더링으로 제한

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    screen.fill((0, 0, 0))

    block.render(screen)
    board.render(screen)

    pygame.display.update() # 화면에 screen 에 내용을 나타내는 함수
