#!/usr/bin/env python
# encoding: utf-8
import curses

class Board(object):

    def __init__(self, ylen=20, xlen=80, ystart=0, xstart=0):
        self._ylen = ylen
        self._xlen = xlen
        self._ystart = ystart
        self._xstart = xstart

    def __enter__(self):
        curses.initscr()
        win = curses.newwin(20, 60, 0, 0)
        win.keypad(1)
        curses.noecho()
        curses.curs_set(0)
        win.border()
        win.nodelay(0)
        self._win = win
        return self
    
    def __exit__(self, *args):
        key = self._win.getch()
        curses.endwin()
    
if __name__ == '__main__':
    with Board() as board:
        pass
