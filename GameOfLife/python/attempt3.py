#!/usr/bin/env python
# encoding: utf-8

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

        new_array = []
        for y in xrange(0, self._ylen):
            new_array_row = []
            for x in xrange(0, self._xlen):
                new_array_row.append(compute_next_cell_gen(x, y))

            new_array.append(new_array_row)



# -------------------------------------------------------------------------------

def test_init():
    test_array = [ [ 1, 1, 1, 1, 1], 
                  [ 1, 1, 1, 1, 1], 
                  [ 1, 1, 1, 1, 1], 
                  [ 1, 1, 1, 1, 1] ]

    grid = Grid()
    grid.init_grid_from(test_array)

    print grid.display_grid()
    assert grid.shape() == (5, 4)


