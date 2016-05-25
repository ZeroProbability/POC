#!/usr/bin/env python
# encoding: utf-8

if __name__ == '__main__':
    main()

class Grid(object):

    """Docstring for Grid. """

    def __init__(self, grid=None):
        if grid is None:
            self._grid = []
            self._lenx = self._leny = 0
        else:
            self.grid = grid
            self._leny = len(grid)
            if self._leny:
                self._lenx = len(grid[0])
            else:
                self._lenx = 0

    def _compute_next_cell(self, y, x):
        xmin = 0 if x == 0 else x -1
        xmax = self._lenx - 1 if x == self._lenx - 1 else x + 1

    def compute_next_grid(self):
        new_grid = []
        for y in self._leny:
            new_grid_row = []
            for x in self._lenx:
                new_grid._row.append(self._compute_next_cell(y, x))



def main():
    print "hello world"

#-------------------------------------------------------------------------------

def test_nothing():
    grid = Grid([[0,0], [1,1]])
    
    assert 1 == 2
