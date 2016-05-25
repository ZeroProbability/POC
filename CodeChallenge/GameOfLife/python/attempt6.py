#!/usr/bin/env python
# encoding: utf-8
from tkinter import *
import random
import time

class Grid(object):

    """Docstring for Grid. """

    def __init__(self, grid=None):
        if grid is None:
            self._grid = []
            self._lenx = self._leny = 0
        else:
            self._grid = grid
            self._leny = len(grid)
            if self._leny:
                self._lenx = len(grid[0])
            else:
                self._lenx = 0

    def _compute_next_cell(self, y, x):
        xmin = 0 if x == 0 else x -1
        xmax = self._lenx - 1 if x == self._lenx - 1 else x + 1

        ymin = 0 if y == 0 else y -1
        ymax = self._leny - 1 if y == self._leny - 1 else y + 1

        total_live_neighbours = 0
        for xi in xrange(xmin, xmax + 1):
            for yi in xrange(ymin, ymax + 1):
                total_live_neighbours += self._grid[yi][xi]

        total_live_neighbours -= self._grid[y][x]

        if self._grid[y][x]: # is alive
            return 1 if total_live_neighbours in (2, 3) else 0
        else:
            return 1 if total_live_neighbours == 3 else 0

    def compute_next_grid(self):
        new_grid_array = []
        for y in xrange(self._leny):
            new_grid_array_row = []
            for x in xrange(self._lenx):
                new_grid_array_row.append(self._compute_next_cell(y, x))

            new_grid_array.append(new_grid_array_row)

        return Grid(new_grid_array)

class MyWorld(object):

    def __init__(self):
        master = Tk()
        self.w = Canvas(master, width=800, height=600)
        self.w.create_rectangle(20, 20, 20, 20, fill="#FF0000", width=0)
        self.w.pack()

        grid_array = []
        for y in xrange(600/20):
            row = []
            for x in xrange(800/20):
                row.append(random.randint(0, 1))
            grid_array.append(row)

        self._grid = Grid(grid_array)
        self.draw_grid(self._grid)

        mainloop()

    def draw_cell(self, y, x, alive=True):
        ystart = y * 20
        xstart = x * 20
        import pdb; pdb.set_trace()
        time.sleep(1)

        if alive:
            fill_color = "#55FF55"
        else:
            fill_color = "#FF0000"
        self.w.create_rectangle(xstart, ystart, 20, 20, fill=fill_color, width=1)

    def draw_grid(self, grid):
        grid_array = grid._grid
        for x in xrange(800/20):
            for y in xrange(600/20):
                self.draw_cell(y, x, grid_array[y][x] == 1)

        self.w.update()

    def start_universe(self):
        grid = grid.compute_next_grid()

def main():
    x = MyWorld()

if __name__ == '__main__':
    main()

#-------------------------------------------------------------------------------

def test_nothing():
    test_grid_array =  [
        [ 0, 0, 0, 0 ], 
        [ 0, 1, 1, 0 ], 
        [ 0, 1, 1, 0 ], 
        [ 0, 1, 1, 0 ], 
        [ 0, 0, 0, 0 ] 
    ]

    grid = Grid(test_grid_array)
    next_grid = grid.compute_next_grid()

    print next_grid._grid
    
    assert 1 == 2
