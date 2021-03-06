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
        self.w = Canvas(master, width=810, height=610, bg="white")
        self.w.pack()
        self.w.update()

        grid_array = []
        for y in xrange(600/5):
            row = []
            for x in xrange(800/5):
                row.append(random.randint(0, 1))
            grid_array.append(row)

        self._grid = Grid(grid_array)
        self.draw_grid(self._grid)

        self.start()

    def draw_cell(self, y, x, alive=True):
        ystart = y * 5
        xstart = x * 5

        if alive:
            fill_color = "#55FF55"
            r=self.w.create_rectangle(xstart, ystart, xstart + 5, ystart + 5, fill=fill_color, width=0)

    def draw_grid(self, grid):
        self.w.delete("all")
        grid_array = grid._grid
        for x in xrange(800/5):
            for y in xrange(600/5):
                self.draw_cell(y, x, grid_array[y][x] == 1)

        self.w.update()

    def start(self):
        while True:
            self._grid = self._grid.compute_next_grid()
            time.sleep(0.01)
            self.draw_grid(self._grid)

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
    
    assert 0 == 2
