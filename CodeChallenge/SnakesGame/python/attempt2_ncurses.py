#!/usr/bin/env python
# encoding: utf-8
import curses
import time

UP = (-1, 0)
DOWN = (1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)

class Board(object):
    def __init__(self, ylen=80, xlen=30, ystart=0, xstart=0):
        self._ylen = ylen
        self._xlen = xlen
        self._ystart = ystart
        self._xstart = xstart
        
    def __enter__(self):
        curses.initscr()
        win = curses.newwin(20, 60, 0, 0)
        win.keypad(1)
        curses.curs_set(0)
        win.border()
        win.nodelay(1)
        self._win = win
        return self
    
    def __exit__(self, *args):
        curses.endwin()

    def get_user_keypress(self):
        return self._win.getch()

    def draw_char(self, y, x, char):
        self._win.addch(y, x, char)


class Snake(object):

    def __init__(self, coordinates=None, board=None):
        self._coordiantes = [(10, i) for i in xrange(3, 9)] if coordinates is None else coordinates
        self._board = board
        self._direction = RIGHT

    def move(self, direction = None):
        current_head = self._coordiantes[-1]
        new_head = (current_head[0] + self._direction[0], 
                        current_head[1] + self._direction[1])
        self._coordiantes.append(new_head)

        tail = self._coordiantes.pop(0)

    def draw(self):
        for c in self._coordiantes:
            self._board.draw_char(c[0], c[1], '#')

    def draw_head(self):
        if self._board:
            head = self._coordiantes[-1]
            self._board.draw_char(head[0], head[1], '#')

    def remove_tail(self):
        if self._board:
            tail = self._coordiantes.pop(0)
            self._board.draw_char(head[0], head[1], '#')
    
if __name__ == '__main__':
    with Board() as board:
        snake = Snake(board= board)
        snake.draw()
        while True:
            key = board.get_user_keypress()
            snake.move()
            time.sleep(0.05)

#-------------------------------------------------------------------------------

def test_snakemove():
    snake = Snake()

    snake.move()

    assert snake._coordiantes == [(10, i) for i in xrange(4, 10)]

