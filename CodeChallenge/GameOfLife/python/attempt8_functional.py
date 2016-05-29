#!/usr/bin/env python
# encoding: utf-8

LIVE = 1
DEAD = 0

class Cell(object):
    def __init__(self, state):
        self.state = state

    def is_live(self):
        return self.state == LIVE

    def __eq__(self, other):
        return self.state == other.state

    def __repr__(self):
        if self.state == DEAD:
            return 'DEAD'
        return 'LIVE'

LiveCell = Cell(LIVE)
DeadCell = Cell(DEAD)

def compute_next_gen_cell(cell, number_of_neighbours):
    if number_of_neighbours == 3:
        return LiveCell

    if number_of_neighbours < 2 or number_of_neighbours > 4:
        return DeadCell

    return cell

class Grid(object):
    def __init__(self):
        self._live_cells = set()


    def is_live(self, y, x):
        return (y, x) in self._live_cells


    def create_cell_at(self, y, x):
        self._live_cells.add((y,x))


    def get_cell_at(self, y, x):
        if (y, x) in self._live_cells:
            return LiveCell
        return DeadCell


    def live_neighbours_of(self, y, x):
        subset = set()
        for yi in xrange(y-1, y+2):
            for xi in xrange(x-1, x+2): 
                if (yi, xi) == (y, x):
                    continue
                if (yi, xi) in self._live_cells:
                    subset.add((yi ,xi))

        return subset


    def all_neighbours(self):
        superset = set()
        for (y, x) in self._live_cells:
            for yi in xrange(y-1, y+2):
                for xi in xrange(x-1, y+2): 
                    superset.add((yi, xi))

        return superset


def compute_next_grid(grid):
    all_neighbours = grid.all_neighbours()
    new_grid = Grid()
    for (y, x) in all_neighbours:
        live_count = len(grid.live_neighbours_of(y, x))
        print "{} {} => {}".format(y, x, live_count)
        new_cell = compute_next_gen_cell(grid.get_cell_at(y, x), live_count)

        if new_cell == LiveCell:
            new_grid.create_cell_at(y, x)

    return new_grid


def main():
    print "this works!!!"

if __name__ == '__main__':
    main()

#-------------------------------------------------------------------------------

def test_cell():
    dead_cell = DeadCell
    live_cell = LiveCell

    assert dead_cell == compute_next_gen_cell(dead_cell, 2)
    assert live_cell == compute_next_gen_cell(dead_cell, 3)

    assert dead_cell == compute_next_gen_cell(dead_cell, 5)
    assert dead_cell == compute_next_gen_cell(dead_cell, 7)

    assert live_cell == compute_next_gen_cell(live_cell, 2)
    assert live_cell == compute_next_gen_cell(live_cell, 3)

def test_grid():

    grid = Grid()

    live_cell_locations = [ (1, 1), (1, 2), (1, 3) ,
                   (2, 1), (2, 2), (2, 3) ]

    for (y,x) in live_cell_locations:
        grid.create_cell_at(y,x)

    expected = [ (1, 1), (0, 2), (1, 3) ,
                   (2, 1), (3, 2), (2, 3) ]

    new_grid = compute_next_grid(grid)

    assert new_grid._live_cells == set(expected)

