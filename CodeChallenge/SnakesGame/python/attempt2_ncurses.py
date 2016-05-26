#!/usr/bin/env python
# encoding: utf-8
import curses
from curses import win

RIGHT = (0, 1)
LEFT = (0, -1)
UP = (-1, 0)
DOWN = (1, 0)

class Board(object):

    def __init__(self, ystart=0, xstart=0, height=30, width=80):
        self._ystart = ystart
        self._xstart = xstart
        self._height = height
        self._width = width
        self.is_over = False

    def __enter__(self):
        curses.initscr()
        win = curses.newwin(self._height, self._width, self._ystart, self._xstart)
        win.keypad(1)
        curses.noecho()
        curses.curs_set(0)
        win.border()
        win.nodelay(0)
        self._win = win

    def __exit__(self, *args):
        key = self._win.getch()
        curses.endwin()

    def show_score(self):
        pass
        
    def place_apple(self):
        pass

    def addch(self, y, x, char):
        self._win.addch(y, x, char)

class Snake(object):

    def __init__(self, board=None, coordinates=None, direction = None):
        self._board = board
        if coordinates == None:
            self._coordinates = [ (10, 3), (10, 4),(10, 5),(10, 6),(10, 7) ]
        else:
            self._coordinates = coordinates

        if direction == None:
            self._direction = RIGHT
        else:
            self._direction = direction

    def move(self):
        head = self._coordinates[-1]
        new_head = (head[0] + self._direction[0], head[1]+ self._direction[1])

        tail = self._coordinates.pop(0)

        self._coordinates.append(new_head)

    def draw(self):
        for c in self._coordinates:
            self._board.addch(c[0], c[1], '#')

if __name__ == '__main__':
    with Board() as board:
        snake = Snake(board)
        snake.draw()

#-------------------------------------------------------------------------------


def test_snake_move():
    snake = Snake()
    snake.move()

    assert snake._coordinates ==  [  (10, 4),(10, 5),(10, 6),(10, 7), (10, 8) ]
