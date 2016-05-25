#!/usr/bin/env python
# encoding: utf-8
import random
import os

def _translate_to_char(v):
    """ translate ones and zeros to displayable char"""
    return '*' if v else ' '

def _translate_row_to_char(row):
    """ translate ones and zeros to displayable char"""
    return ' '.join([_translate_to_char(x) for x in row])
    

class Grid(object):
    def __init__(self, ylen=0, xlen=0):
        self._xlen = xlen
        self._ylen = ylen
        self._grid = []

    def size(self):
        return self._ylen, self._xlen

    def init_random(self):
        for _ in xrange(self._ylen):
            row = [random.randint(0, 1) for _ in xrange(self._xlen)]
            self._grid.append(row)

    def display(self):
        output = []
        for row in self._grid:
            output.append(_translate_row_to_char(row))

        return '\n'.join(output)

    def init_grid_from(self, two_d_array):
        self._grid=two_d_array

        self._ylen=len(two_d_array)
        if self._ylen:
            self._xlen=len(two_d_array[0])
        else:
            self._xlen=0

        return self

    def neighbors_live_count(self, y, x):
        ymin = 0 if y == 0 else y-1
        xmin = 0 if x == 0 else x-1

        xmax = self._xlen - 1 if x == self._xlen - 1 else x + 1
        ymax = self._ylen - 1 if y == self._ylen - 1 else y + 1

        live_count = 0
        for x1 in xrange(xmin, xmax+1):
            for y1 in xrange(ymin, ymax+1):
                live_count += self._grid[y1][x1]

        live_count -= self._grid[y][x]

        return live_count

    def next_gen_for_cell(self, y, x):
        live_count = self.neighbors_live_count(y, x)

        if self._grid[y][x]:
            if live_count in (2, 3):
                return 1
            else:
                return 0
        else:
            if live_count == 3:
                return 1
            else:
                return 0

    def next_gen_grid(self):
        new_grid = []
        for y in xrange(self._ylen):
            new_grid_row = []
            for x in xrange(self._xlen):
                new_grid_row.append(self.next_gen_for_cell(y, x))
            new_grid.append(new_grid_row)

        return Grid().init_grid_from(new_grid)

if __name__ == '__main__':
    grid = Grid(20, 50)
    grid.init_random()
    while True:
        os.system('clear')
        print grid.display()
        import time
        time.sleep(.1)
        grid = grid.next_gen_grid()


#-------------------------------------------------------------------------------

def test_traslate_row():
    assert _translate_row_to_char([1, 1, 1]) == '* * *'
    assert _translate_row_to_char([1, 0, 1]) == '*   *'
    assert _translate_row_to_char([0, 0, 1]) == '    *'

def test_init():
    grid = Grid(3, 5)
    assert grid.size() == (3, 5)

def test_initalize_by_me():
    test_grid = [
                  [1, 1, 0, 0, 1, 1],
                  [1, 1, 1, 1, 0, 1],
                  [1, 0, 0, 0, 0, 1]
              ]

    grid=Grid()
    grid.init_grid_from(test_grid)

    assert grid.size() == (3, 6)

    assert grid.neighbors_live_count(1, 1) == 5

    assert grid.next_gen_for_cell(1, 1) == 0
    assert grid.next_gen_for_cell(2, 2) == 1
    
