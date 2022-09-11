# -*- coding: utf-8 -*-

# import modules
from sys import exit

from pygame import time
from pygame import init, display, quit
from pygame import event
from pygame import QUIT, MOUSEBUTTONDOWN, KEYDOWN
from pygame import K_LEFT, K_RIGHT, K_DOWN, K_UP, K_RETURN

from config import *
from logic import Game2048
from database import DataBase

if __name__ == '__main__':
    init()
    screen = display.set_mode((WIDTH, HEIGHT))
    display.set_caption('2048')
    db = DataBase()
    game = Game2048(screen, BLOCKS, SIZE_BLOCK, MARGIN, WIDTH, HEIGHT, MAP_2048, PALETTE, db)

    while RUNNING_GAME:
        time.delay(FPS)
        screen.fill(PALETTE[1])
        for event_i in event.get():
            if event_i.type == QUIT:
                quit()
                exit()
            elif event_i.type == MOUSEBUTTONDOWN:
                if event_i.button == 1:
                    if MENU:
                        MENU = game.get_position_mouse()
            elif event_i.type == KEYDOWN:
                if event_i.key == K_LEFT:
                    game.enter_key_left()
                elif event_i.key == K_RIGHT:
                    game.enter_key_right()
                elif event_i.key == K_DOWN:
                    game.enter_key_down()
                elif event_i.key == K_UP:
                    game.enter_key_up()
                elif event_i.key == K_RETURN:
                    game.restart_game()
        if MENU:
            game.draw_menu()
        else:
            game.draw_score()
            game.draw_blocks()
        display.update()

    quit()