#!/usr/bin/env python
# encoding: utf-8

from tkinter import *
from itertools import product


def neigbhours(t):
    y, x = t
    return set(product([y-1, y, y+1], [x-1, x, x+1])) - set([(y,x)])


def array_to_string(array):
    def display_row(row):
        return ''.join([str(c) for c in row])

    row_strings = map(display_row, array)

    return '\n'.join(row_strings)


class Grid(object):

    def __init__(self, grid=None):
        self._grid = grid

    @classmethod
    def init_from(clazz, two_d_array):
        ylen = len(two_d_array)
        xlen = len(two_d_array[0])

        grid = set()
        for x in xrange(xlen):
            for y in xrange(ylen):
                if two_d_array[y][x]:
                   grid.add((y,x))

        return clazz(grid)

    def display(self, xlen, ylen):
        viewport = []
        for y in xrange(ylen):
            row = []
            for x in xrange(xlen):
                row.append(1 if (y,x) in self._grid else 0)
            viewport.append(row)
        return viewport

    def is_alive(self, location):
        return location in self._grid

    def should_be_alive(self, location):
        n = neigbhours(location)
        if self.is_alive(location):
            return len(filter(self.is_alive, n)) in (2,3)
        else:
            return len(filter(self.is_alive, n)) == 3

    def compute_next(self):
        cells_to_consider =  reduce(lambda se, ne: se.union(ne), map(neigbhours, self._grid), set([]))
        cells_alive_in_next = filter(self.should_be_alive, cells_to_consider)
        return Grid(cells_alive_in_next)

if __name__ == '__main__':
    import numpy as np
    rand_array = np.random.randint(0, 2, (40, 80))
    rand_array = map(list, rand_array)
    grid = Grid.init_from(rand_array)
    while True:
        grid = grid.compute_next()
        next_array = grid.display(80, 40 )
        import os; os.system('clear')
        print array_to_string(next_array).replace('0', ' ').replace('1', '*')

        import time; time.sleep(0.01)


#-------------------------------------------------------------------------------

def test_grid_cast1():
    test_grid = [[ 0, 0, 0, 0  ], 
                 [ 0, 1, 1, 0  ], 
                 [ 0, 1, 1, 0  ], 
                 [ 0, 1, 1, 0  ], 
                 [ 0, 0, 0, 0  ]] 

    grid = Grid.init_from(test_grid)

    assert test_grid == grid.display(4, 5)

    next_grid_as_array = grid.compute_next().display(4, 5)

    assert next_grid_as_array == [[ 0, 0, 0, 0  ], 
                 [ 0, 1, 1, 0  ], 
                 [ 1, 0, 0, 1  ], 
                 [ 0, 1, 1, 0  ], 
                 [ 0, 0, 0, 0  ]] 
