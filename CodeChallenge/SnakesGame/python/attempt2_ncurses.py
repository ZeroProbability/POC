#!/usr/bin/env python
# encoding: utf-8
import curses
import time

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
        win.nodelay(1)
        self._win = win
        return self

    def __exit__(self, *args):
        curses.endwin()

    def show_score(self):
        pass
        
    def place_apple(self):
        pass

    def addch(self, y, x, char):
        self._win.addch(y, x, char)

    def addstr(self, y, x, string):
        self._win.addstr(y, x, string)

class Snake(object):

    def __init__(self, board, coordinates=None, direction = None):
        self._board = board
        if coordinates == None:
            self._coordinates = [ (10, 3), (10, 4),(10, 5),(10, 6),(10, 7) ]
        else:
            self._coordinates = coordinates

        if direction == None:
            self._direction = RIGHT
        else:
            self._direction = direction

    def move(self, key=None):
        if key == curses.KEY_UP and not self._direction == DOWN:
            self._direction == UP

        head = self._coordinates[-1]
        new_head = (head[0] + self._direction[0], head[1]+ self._direction[1])

        tail = self._coordinates.pop(0)

        self._coordinates.append(new_head)

        if not self._board is None:
            self._board.addch(new_head[0], new_head[1], '#')
            self._board.addch(tail[0], tail[1], ' ')


    def draw(self):
        for c in self._coordinates:
            self._board.addch(c[0], c[1], '#')

if __name__ == '__main__':
    with Board() as board:
        snake = Snake(board=board)
        snake.draw()
        while True:
            key = board._win.getch()
            snake.move(key)
            time.sleep(0.05)

#-------------------------------------------------------------------------------


def test_snake_move():
    snake = Snake()
    snake.move()

    assert snake._coordinates ==  [  (10, 4),(10, 5),(10, 6),(10, 7), (10, 8) ]
