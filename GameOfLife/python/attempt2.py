#!/usr/bin/env python
# encoding: utf-8
import random
import os

class Grid(object):
    def __init__(self, xlen, ylen):
        self._xlen = xlen
        self._ylen = ylen
        self._grid = []

    def size(self):
        return self._xlen, self._ylen

    def init_random(self):
        for _ in self._ylen:
            row = [random.randint(0, 1) for _ in self._xlen]
            self._grid.append(row)

    def display(self):
        for y in self._ylen:



if __name__ == '__main__':
    main()

#-------------------------------------------------------------------------------

def test_init():
    grid = Grid(3, 5)
    assert grid.size() == (3, 5)

