import copy
import random
from constants import ALIVE, DEAD, RANDOM_PROBABILITY


def get_board(size):
    """
    Генерирование доски
    :param size:
    :return:
    """
    mas = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            rnd = random.randint(0, 100)
            if rnd > RANDOM_PROBABILITY:
                mas[i][j] = ALIVE
            else:
                mas[i][j] = DEAD
    return mas


def print_board(cells):
    """
    Печать доски
    :param cells:
    :return:
    """
    for i in range(len(cells)):
        row_to_print = []
        for j in range(len(cells)):
            if cells[i][j] == ALIVE:
                row_to_print.append('o')
            else:
                row_to_print.append(' ')
        print(' '.join(row_to_print))


def get_neighbours(cells, x: int, y: int):
    """
    Получение количества живых соседей
    :param cells:
    :param x:
    :param y:
    :return:
    """
    count = 0
    inds = [-1, 0, 1]
    for i in inds:
        for j in inds:
            new_x = x + i
            new_y = y + j
            if i == j == 0 or new_x < 0 or new_x >= len(cells) or new_y < 0 or new_y >= len(cells):
                continue

            if cells[new_x][new_y] == ALIVE:
                count += 1
    return count


def check_status(cells, x, y):
    """
    Проверка статус ячейки
    :param cells:
    :param x:
    :param y:
    :return:
    """
    cell = cells[x][y]
    neigh = get_neighbours(cells, x, y)
    if cell == ALIVE:
        if 2 <= neigh <= 3:
            return ALIVE
        else:
            return DEAD

    if cell == DEAD and neigh == 3:
        return ALIVE

    return cell


def get_next_gen(board):
    """
    Получение следующего поколения
    :param board:
    :return:
    """
    old = copy.deepcopy(board)
    for i in range(len(board)):
        for j in range(len(board)):
            board[i][j] = check_status(old, i, j)
