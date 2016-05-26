#!/usr/bin/env python
# encoding: utf-8

import curses
import random

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

class Board(object):
    def __init__(self, beginx=0, beginy=0, width=80, height=30):
        self._beginx = beginx
        self._beginy = beginy
        self._width = width
        self._height = height

    def __enter__(self):
        curses.initscr()                        
        win = curses.newwin(self._height, self._width, self._beginy, self._beginx)       
               # height, width, top, left       
        win.keypad(1)                           
        curses.noecho()                         
        curses.curs_set(0)                      
        win.border()                            
        win.nodelay(1)                          
        self._win = win
        self._game_over = False
        self.place_apple()
        return self

    def __exit__(self, *args):
        key = self._win.getch()                       
        curses.endwin()

    def draw_char(self, y, x, char):
        self._win.addch(y, x, char)

    def getch(self):
        return self._win.getch()

    def place_apple(self):
        x = random.randint(1, self._width-2)
        y = random.randint(1, self._height-2)

        self.draw_char(y, x, '*')

    def endgame(self):
        self._win.addstr(3, 3, "Game over!!")
        self._game_over = True

class Snake(object):
    def __init__(self, board):
        self._cordinates = [(10,3), (10,4), (10,5), (10, 6), (10, 7), (10, 8)]
        self._cordinates
        self._direction = RIGHT
        self._board = board

    def move(self):
        if self._board._game_over:
            return

        head = list(self._cordinates[-1])
        head[0] += self._direction[0]
        head[1] += self._direction[1]

        if head[0] in (self._board._beginy, self._board._beginy + self._board._height - 1)  \
            or head[1] in ( self._board._beginx, self._board._beginx + self._board._width - 1) \
            or tuple(head) in self._cordinates:
                self._board.endgame()

        self._cordinates.append(tuple(head))
        self._board.draw_char(head[0], head[1], '#')
        tail = self._cordinates.pop(0)
        self._board.draw_char(tail[0], tail[1], ' ')

    def draw(self):
        for c in self._cordinates:
            self._board.draw_char(c[0], c[1], '#')

    def change_direction(self, key):
        if key == curses.KEY_LEFT and not self._direction == RIGHT:
            self._direction = LEFT
        elif key == curses.KEY_RIGHT and not self._direction == LEFT:
            self._direction = RIGHT
        elif key == curses.KEY_UP and not self._direction == DOWN:
            self._direction = UP
        elif key == curses.KEY_DOWN and not self._direction == UP:
            self._direction = DOWN
        else:
            pass

if __name__ == '__main__':
    with Board() as b:
        snake = Snake(b)
        snake.draw()
        while True:
            snake.move()
            user_key = b.getch()
            snake.change_direction(user_key)
            import time; time.sleep(0.1)
