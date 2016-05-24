#!/usr/bin/env python
# encoding: utf-8
import pandas as pd
import numpy as np
import time
import os
from numba import jit

pd.options.display.max_rows = 999
pd.options.display.max_columns = 999
pd.options.display.width = 999

class Grid(object):

    def __init__(self, ylen, xlen):
        self._grid = pd.DataFrame(np.zeros(shape=(ylen, xlen)))

    def init_random(self):
        ylen, xlen = self._grid.shape
        random_int_array = np.random.randint(0, 2, xlen*ylen)
        self._grid = pd.DataFrame(np.reshape(random_int_array, (ylen, xlen)))

    def live_neighbours_count(self, y, x):
        neighbours = self._grid.loc[y-1: y+1, x-1: x+1] 
        return neighbours.as_matrix().sum().sum() - self._grid[x][y]

    @jit
    def compute_next_gen_of(self, y, x):
        count = self.live_neighbours_count(y, x)
        next_gen_is_alive =  \
               ( self._grid[x][y] and count in (2, 3)) \
                   or \
               ( self._grid[x][y] == 0 and count == 3 )

        return int(next_gen_is_alive)

    @jit
    def compute_next_grid(self):
        ylen, xlen = self._grid.shape
        new_df = pd.DataFrame(np.zeros(shape=(ylen, xlen)))
        for y in xrange(ylen):
            for x in xrange(xlen):
                new_df[x][y] = self.compute_next_gen_of(y, x)
        new_grid = Grid(ylen, xlen)
        new_grid._grid = new_df
        return new_grid

    def display(self):
        return self._grid.replace(0, ' ').replace(1, '*')
        
    def __repr__(self):
        return self._grid.__repr__()

if __name__ == '__main__':
    grid= Grid(20, 40)
    grid.init_random()

    for _ in xrange(1, 100):
        print grid.display()
        grid = grid.compute_next_grid()
        time.sleep(0.1)
        os.system('clear')

