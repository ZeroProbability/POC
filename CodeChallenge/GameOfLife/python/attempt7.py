#!/usr/bin/env python
# encoding: utf-8
import os
import random
import time

class Grid(object):

    def __init__(self, leny=0, lenx=0, array=None):
        self._leny = leny
        self._lenx = lenx
        self._grid_array = array

    @classmethod
    def from_array(clazz, array):
        inst = clazz()

        inst._leny = len(array)
        inst._lenx = len(array[0])

        inst._grid_array = array

        return inst

    def init_random(self):
        grid_array = []
        for y in xrange(self._leny):
            grid_row = []
            for x in xrange(self._lenx):
                grid_row.append(random.randint(0,1))

            grid_array.append(grid_row)

        self._grid_array = grid_array

    def compute_next_at(self, y, x):
        miny = 0 if y == 0 else y - 1
        minx = 0 if x == 0 else x - 1

        maxy = self._leny - 1 if y == self._leny - 1 else y + 1
        maxx = self._lenx - 1 if x == self._lenx - 1 else x + 1

        neighbour_count=0
        for y1 in xrange(miny, maxy+1):
            for x1 in xrange(minx, maxx+1):
                neighbour_count += self._grid_array[y1][x1]

        neighbour_count -= self._grid_array[y][x]

        if self._grid_array[y][x]: # is alive
            return 1 if neighbour_count in (2, 3) else 0
        else:
            return 1 if neighbour_count == 3 else 0


    def compute_next_array(self):
        new_grid_array = []
        for y in xrange(self._leny):
            new_grid_array_row = []
            for x in xrange(self._lenx):
                new_value = self.compute_next_at(y, x)
                new_grid_array_row.append(new_value)
            new_grid_array.append(new_grid_array_row)

        return new_grid_array

    def cell_alive_at(self, y, x):
        return self._grid_array[y][x] == 1

class GridView(object):

    def __init__(self, grid):
        self.grid = grid

    def set_grid(self, grid):
        self.grid = grid

    def render(self):
        for y in xrange(self.grid._leny):
            for x in xrange(self.grid._lenx):
                print '*' if self.grid.cell_alive_at(y, x) else ' ',
            print ''


if __name__ == '__main__':
    grid = Grid(leny=50, lenx=80)
    grid.init_random()
    gv = GridView(grid)

    while(True):
        os.system('clear')
        gv.render()
        time.sleep(0.1)
        new_grid_array = grid.compute_next_array()
        grid = Grid.from_array(new_grid_array)
        gv.set_grid(grid)
        

#-------------------------------------------------------------------------------

def test_grid():
    test_grid_array = [
                [ 0, 0, 0, 0, 0],
                [ 0, 1, 1, 1, 0],
                [ 0, 1, 1, 1, 0],
                [ 0, 0, 0, 0, 0]
        ]

    grid = Grid.from_array(test_grid_array)

    new_array = grid.compute_next_array()

    print new_array

    assert new_array == [
                [ 0, 0, 1, 0, 0],
                [ 0, 1, 0, 1, 0],
                [ 0, 1, 0, 1, 0],
                [ 0, 0, 1, 0, 0]
        ]


