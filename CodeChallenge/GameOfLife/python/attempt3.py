#!/usr/bin/env python
# encoding: utf-8

import os

class Grid(object):

    def __init__(self, xlen=0, ylen=0):
        self._xlen = xlen
        self._ylen = ylen

        self._grid = []

    def init_grid_from(self, two_d_array):
        self._grid = two_d_array

        self._ylen = len(two_d_array)

        if self._ylen:
            self._xlen = len(two_d_array[0])

        return self


    def display_grid(self):
        def display_row(row):
            return ''.join([str(c) for c in row])

        row_strings = map(display_row, self._grid)

        return '\n'.join(row_strings)

    def shape(self):
        return self._xlen, self._ylen

    def compute_next_gen(self):
        def compute_next_cell_gen(x, y):
            xmin = 0 if x == 0 else x - 1
            ymin = 0 if y == 0 else y - 1
            xmax = self._xlen - 1 if x == self._xlen - 1 else x + 1
            ymax = self._ylen - 1 if y == self._ylen - 1 else y + 1

            live_neighbours=0
            for x1 in xrange(xmin, xmax + 1):
                for y1 in xrange(ymin, ymax+1):
                    live_neighbours += self._grid[y1][x1]

            live_neighbours -= self._grid[y][x]

            if self._grid[y][x]:
                return 1 if live_neighbours in (2, 3) else 0
            else:
                return 1 if live_neighbours == 3 else 0

        new_array = []
        for y in xrange(0, self._ylen):
            new_array_row = []
            for x in xrange(0, self._xlen):
                new_array_row.append(compute_next_cell_gen(x, y))

            new_array.append(new_array_row)

        return Grid().init_grid_from(new_array)


if __name__ == '__main__':

    import numpy as np
    rand_array = np.random.randint(0, 2, (20, 80))
    rand_array = map(list, rand_array)
    grid = Grid().init_grid_from(rand_array)


    while True:
        os.system('clear')
        print grid.display_grid().replace('0', ' ').replace('1', '*')

        import time; time.sleep(0.1)
        grid = grid.compute_next_gen()

# -------------------------------------------------------------------------------

def test_init():
    test_array = [ [ 0, 0, 0, 0, 0], 
                  [ 0, 1, 1, 1, 0], 
                  [ 0, 1, 1, 1, 0], 
                  [ 0, 0, 0, 0, 0] ]

    grid = Grid()
    grid.init_grid_from(test_array)

    assert grid.shape() == (5, 4)

    computed_str = grid.compute_next_gen().display_grid()

    assert computed_str == "00100\n" + "01010\n" + "01010\n" + "00100"

