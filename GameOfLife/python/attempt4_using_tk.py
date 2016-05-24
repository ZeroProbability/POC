#!/usr/bin/env python
# encoding: utf-8

from tkinter import *
from itertools import product


def neigbhours(t):
    y, x = t
    return set(product([y-1, y, y+1], [x-1, x, x+1])) - set([(y,x)])

def should_be_alive(is_alive, neigbhours):
    if is_alive:
        return len(neigbhours) in (2,3)
    else:
        return len(neigbhours) == 3

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

    def compute_next(self):
        cells_to_consider =  reduce(lambda se, ne: se.union(ne), map(neigbhours, self._grid), set([]))


#-------------------------------------------------------------------------------

def test_grid_cast1():
    test_grid = [[ 0, 0, 0, 0  ], 
                 [ 0, 1, 1, 0  ], 
                 [ 0, 1, 1, 0  ], 
                 [ 0, 1, 1, 0  ], 
                 [ 0, 0, 0, 0  ]] 

    grid = Grid.init_from(test_grid)

    assert test_grid == grid.display(4, 5)

    print grid.compute_next()

    assert 1 == 2
