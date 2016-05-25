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

        


def main():
    print "hello world"

#-------------------------------------------------------------------------------

def test_nothing():
    grid = Grid([[0,0], [1,1]])
    
    assert 1 == 2
