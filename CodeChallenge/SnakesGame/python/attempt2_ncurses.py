#!/usr/bin/env python
# encoding: utf-8
import curses
import time
import random
from unittest import MagicMock

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
        self.apple_location = self.place_apple()
        
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

    def place_apple(self):
        apple_y = random.randint(self._ystart+1, self._ystart + self._ylen-2)
        apple_x = random.randint(self._xstart+1, self._xstart + self._xlen-2)
        self._win.addch(y, x, '*')
        return (apple_y, apple_x)

class Snake(object):

    def __init__(self, coordinates=None, board=None):
        self._coordiantes = [(10, i) for i in xrange(3, 9)] if coordinates is None else coordinates
        self._board = board
        self._direction = RIGHT

    def ate_apple(self):
        ate_it = self._board.apple_location == self._coordiantes[-1]
        if ate_it:
            self._board.place_apple()

        return ate_it

    def move(self, direction = None):
        if direction is None:
            direction = self._direction
        else:
            if self._direction == UP and direction == DOWN:
                direction = UP
            elif self._direction == DOWN and direction == UP:
                direction = DOWN
            elif self._direction == RIGHT and direction == LEFT:
                direction = RIGHT
            elif self._direction == LEFT and direction == RIGHT:
                direction = LEFT

        self._direction = direction

        current_head = self._coordiantes[-1]
        new_head = (current_head[0] + direction[0], 
                        current_head[1] + direction[1])
        self._coordiantes.append(new_head)

        tail = self._coordiantes.pop(0)

        self.draw_head() 
        if not self.ate_apple():
            self.remove_tail(tail)

    def draw(self):
        for c in self._coordiantes:
            self._board.draw_char(c[0], c[1], '#')

    def draw_head(self):
        if self._board:
            head = self._coordiantes[-1]
            self._board.draw_char(head[0], head[1], '#')

    def remove_tail(self, tail):
        if self._board:
            self._board.draw_char(tail[0], tail[1], ' ')
    
if __name__ == '__main__':
    with Board() as board:
        snake = Snake(board= board)
        snake.draw()
        while True:
            key = board.get_user_keypress()
            if key == curses.KEY_UP:
                snake.move(UP)
            elif key == curses.KEY_DOWN:
                snake.move(DOWN)
            elif key == curses.KEY_RIGHT:
                snake.move(RIGHT)
            elif key == curses.KEY_LEFT:
                snake.move(LEFT)
            else:
                snake.move()
                
            time.sleep(0.05)

#-------------------------------------------------------------------------------

def test_snakemove():
    board = Board()
    snake = Snake(board = board)

    snake.move()
    assert snake._coordiantes == [(10, i) for i in xrange(4, 10)]

    snake.move(UP)
    assert snake._coordiantes == [(10, i) for i in xrange(5, 10)] + [(9, 9)]

    snake.move(DOWN)
    assert snake._coordiantes == [(10, i) for i in xrange(6, 10)] + [(9, 9), (8, 9)]

    board.apple_location = (7, 9)
    snake.move()

    assert snake._coordiantes == [(10, i) for i in xrange(6, 10)] + [(9, 9), (8, 9), (7, 9)]

