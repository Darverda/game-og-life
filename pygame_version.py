from pygame import *
import pygame
import sys
from constants import WHITE, BLACK
from core import *
import time


def draw(screen, main_surface, board):
    """
    Отрисовка ячеек
    :param screen:
    :param main_surface:
    :param board:
    :return:
    """
    for x in range(len(board)):
        for y in range(len(board)):
            if board[x][y] == ALIVE:
                pygame.draw.rect(main_surface, BLACK, (x * 10, y * 10, 10, 10))
            else:
                pygame.draw.rect(main_surface, WHITE, (x * 10, y * 10, 10, 10))
    screen.blit(main_surface, (0, 0))

def run(size):
    """
    Запуск
    :param size:
    :return:
    """
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    main_surface = pygame.Surface((500, 500))
    main_surface.fill(WHITE)

    board = get_board(size)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        get_next_gen(board)

        draw(screen, main_surface, board)
        screen.blit(main_surface, (0, 0))
        pygame.display.update()
        time.sleep(0.2)


if __name__ == "__main__":
    size = 50
    run(size)