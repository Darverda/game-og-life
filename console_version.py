from os import system
from time import sleep
from core import *


def run(size):
    """
    Запуск симуляции
    :param size:
    :return:
    """
    board = get_board(size)
    while True:
        system('cls')
        get_next_gen(board)
        print_board(board)
        sleep(1)


if __name__ == "__main__":
    size = 30
    run(size)
