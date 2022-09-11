# -*- coding: utf-8 -*-

# import modules
from sys import exit

from pygame import font, draw
from pygame import quit
from pygame import mouse

from math import ceil
from random import random, choice


class Game2048:
    def __init__(self, _screen, _count, _size, _margin, _w, _h, _map, _palette, _db):
        self.screen = _screen
        self.count = _count
        self.size = _size
        self.margin = _margin
        self.w = _w
        self.h = _h
        self.map = _map
        self.db = _db
        self.score = 0
        self.plus = 0
        self.style1 = font.SysFont('Consolas', 20)
        self.style2 = font.SysFont('simsun', ceil(self.size / 2))
        self.style3 = font.SysFont('Consolas', 17)
        self.style4 = font.SysFont('Consolas', ceil(self.size / 2))
        self.COLORS = _palette
        self.menu = (
            (0, '2048'),
            (1, 'Start'),
            (2, 'Quit'),
        )
        self.COUNT_M = len(self.menu)

    def draw_menu(self):
        # Список позиций пунктов МЕНЮ [ x, y, width, height ]
        self.pos = []
        # Отрисовываем ФОН
        draw.rect(self.screen, self.COLORS[1], (0, 0, self.w, self.h))
        # Получаем координаты МЫШИ
        x, y = mouse.get_pos()
        # Формируем компоненты МЕНЮ
        for i in range(self.COUNT_M):
            text = self.style4.render(self.menu[i][1], True, self.COLORS[2])
            if self.menu[i][0] == 0:
                text = self.style4.render(self.menu[i][1], True, self.COLORS[8])
            text_w, text_h = text.get_size()
            self.pos += [
                [
                    # [ x, y, width, height ]
                    (self.w - text_w)/2,
                    (self.h - text_h*self.COUNT_M)/2 + i*(text.get_size()[1] + 5),
                    text_w,
                    text_h
                ]
            ]
            # Определяем, находится ли курсор в зоне МЕНЮ
            if self.pos[i][0] <= x <= self.pos[i][0] + self.pos[i][2] and \
                    self.pos[i][1] <= y <= self.pos[i][1] + self.pos[i][3] and self.menu[i][0] != 0:
                text = self.style4.render(self.menu[i][1], True, self.COLORS[4])
            self.screen.blit(text, (self.pos[i][0], self.pos[i][1]))

    def draw_score(self):
        draw.rect(self.screen, self.COLORS[3], (0, 0, self.w, self.h - self.w))

        enter = self.style3.render('Press [Enter] to restart the game', True, self.COLORS[512])
        record = self.style1.render('record: %s' % self.score, True, self.COLORS[8])
        score = self.style1.render('score:  %s' % self.score, True, self.COLORS[0])
        pscore = self.style3.render('+%s' % self.plus, True, self.COLORS[32])

        height = record.get_size()[1]

        self.screen.blit(enter, ((self.w - enter.get_size()[0])/2, 10))
        self.screen.blit(record, (10, (self.h - self.w - height)/2))
        self.screen.blit(score, (10, (self.h - self.w - height)/2 + height))

        if self.plus > 0:
            self.screen.blit(pscore, (120, (self.h - self.w - height)/2 + height*2))

    def draw_blocks(self):
        for i in range(self.count):
            for j in range(self.count):
                w = j * self.size + (j + 1)*self.margin
                h = i * self.size + (i + 1)*self.margin + (self.h - self.w)
                if self.map[i][j] == 2 or self.map[i][j] == 4:
                    BLACK_or_WHITE = self.COLORS[3]
                else:
                    BLACK_or_WHITE = self.COLORS[5]
                value = self.style2.render(str(self.map[i][j]), True, BLACK_or_WHITE)
                draw.rect(self.screen, self.COLORS[self.map[i][j]], (w, h, self.size, self.size))
                if self.map[i][j] != 0:
                    text_x = w + (self.size - value.get_size()[0])/2
                    text_y = h + (self.size - value.get_size()[1])/2
                    self.screen.blit(value, (text_x, text_y))

    def get_position_mouse(self):
        # Определяем попадание по пунктам меню
        # Получаем координаты МЫШИ
        x, y = mouse.get_pos()
        # Определяем, находится ли курсор в зоне МЕНЮ
        for i in range(self.COUNT_M):
            if self.pos[i][0] <= x <= self.pos[i][0] + self.pos[i][2] and \
    self.pos[i][1] <= y <= self.pos[i][1] + self.pos[i][3]:
                if self.menu[i][0] == 1:
                    # Запускаем игру
                    self.map = [[0] * self.count for _ in range(self.count)]
                    if len(self.menu) > 3:
                        # Убираем из меню всё ненужное
                        self.menu = self.menu[:3]
                    return False
                if self.menu[i][0] == 2:
                    # Выходим из игры
                    quit()
                    exit()
        return True

    def generating_an_empty_map(self, value=None):
        if value is not None:
            return [[value] * self.count for _ in range(self.count)]
        return [[] * self.count for _ in range(self.count)]

    def delete_a_random_element(self, map):
        block_number = []
        value = None
        for i in range(self.count):
            for j in range(self.count):
                if map[i][j] == 0:
                    block_number.append((j + 1) + i * self.count)
        if block_number:
            value = choice(block_number)
            block_number.remove(value)
        return value

    def create_block_2_or_4(self, map, value):
        for i in range(self.count):
            for j in range(self.count):
                if (j + 1) + i * self.count == value:
                    if random() <= 0.75:
                        map[i][j] = 2
                    else:
                        map[i][j] = 4
        return map

    def append_0_to_the_end(self, map):
        self.plus = 0
        for row in map:
            while 0 in row:
                row.remove(0)
            while len(row) < self.count:
                row.append(0)
        for i in range(self.count):
            for j in range(self.count - 1):
                if map[i][j] == map[i][j + 1] and map[i][j] != 0:
                    map[i][j] *= 2
                    self.score += map[i][j]
                    self.plus += map[i][j]
                    map[i].pop(j + 1)
                    map[i].append(0)
        return map

    def append_0_to_the_begin(self, map):
        self.plus = 0
        for row in map:
            while 0 in row:
                row.remove(0)
            while len(row) < self.count:
                row.insert(0, 0)
        for i in range(self.count):
            for j in range(self.count - 1, 0, -1):
                if map[i][j] == map[i][j - 1] and map[i][j] != 0:
                    map[i][j] *= 2
                    self.score += map[i][j]
                    self.plus += map[i][j]
                    map[i].pop(j - 1)
                    map[i].insert(0, 0)
        return map

    def enter_key_left(self):
        self.map = self.append_0_to_the_end(self.map)
        value = self.delete_a_random_element(self.map)
        self.map = self.create_block_2_or_4(self.map, value)

    def enter_key_right(self):
        self.map = self.append_0_to_the_begin(self.map)
        value = self.delete_a_random_element(self.map)
        self.map = self.create_block_2_or_4(self.map, value)

    def enter_key_up(self):
        map = self.generating_an_empty_map()
        for j in range(self.count):
            for i in range(self.count):
                map[j].append(self.map[i][j])
        map = self.append_0_to_the_end(map)
        self.map = self.generating_an_empty_map()
        for j in range(self.count):
            for i in range(self.count):
                self.map[j].append(map[i][j])
        value = self.delete_a_random_element(self.map)
        self.map = self.create_block_2_or_4(self.map, value)

    def enter_key_down(self):
        map = self.generating_an_empty_map()
        for j in range(self.count):
            for i in range(self.count):
                map[j].append(self.map[i][j])
        map = self.append_0_to_the_begin(map)
        self.map = self.generating_an_empty_map()
        for j in range(self.count):
            for i in range(self.count):
                self.map[j].append(map[i][j])
        value = self.delete_a_random_element(self.map)
        self.map = self.create_block_2_or_4(self.map, value)

    def restart_game(self):
        self.map = self.generating_an_empty_map(0)
        self.score = 0
        self.plus = 0
