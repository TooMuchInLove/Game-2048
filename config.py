# -*- coding: utf-8 -*-

# Частота кадров
FPS = 100

# Количество блоков
BLOCKS = 5
# Размер блока
SIZE_BLOCK = 100
# Расстояние между
MARGIN = int(SIZE_BLOCK*10 / 100)
# Ширина рабочего окна
WIDTH = MARGIN + (SIZE_BLOCK + MARGIN) * BLOCKS
# Высота рабочего окна
HEIGHT = WIDTH + 100

# Для игрового цикла
RUNNING_GAME = True
# Меню игры
MENU = True

# Игровая карта
MAP_2048 = [[0] * BLOCKS for _ in range(BLOCKS)]

# Палитра цветов
PALETTE = {
    0    : (255, 254, 222),
    1    : ( 26,  26,  26),
    2    : (255, 254, 200),
    3    : ( 10,  10,  10),
    4    : (255, 219, 110),
    5    : (255, 255, 255),
    8    : (252, 177,  19),
    16   : (244, 116,  58),
    32   : (242,  86,  74),
    64   : (239,  53, 104),
    128  : (242, 112, 148),
    256  : (211, 162, 187),
    512  : (154, 147, 159),
    1024 : ( 68, 108, 107),
    2048 : (  0,  51,  38),
}