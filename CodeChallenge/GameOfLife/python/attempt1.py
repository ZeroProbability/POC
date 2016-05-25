#!/usr/bin/env python
# encoding: utf-8

# False is dead, True is live

import os

class GridCell(object):
    def __init__(self, x=0, y=0, live=False):
        self._x = x
        self._y = y
        self._live = live

    def get_location(self):
        return self._x, self._y

    def is_live(self):
        return self._live

    def evaluate_next(self, grid):
        neighbours = grid.get_cells_around(self)
        count_of_live = reduce(lambda s,x: s + (1 if x.is_live() else 0), neighbours, 0)
        new_one_live = self._live
        if self._live:
            if count_of_live < 2 or count_of_live > 3:
                new_one_live = False
        else:
            if count_of_live == 3:
                new_one_live = True
        return GridCell(self._x, self._y, new_one_live)

    def __repr__(self):
        return "({}, {}) {}".format(self._x, self._y, self._live)
        
class DeadCell(GridCell):
    def __init__(self, x=0, y=0):
        super(DeadCell).__init__(x, y, False)

class LiveCell(GridCell):
    def __init__(self, x=0, y=0):
        super(DeadCell).__init__(x, y, False)

class Grid(object):
    def __init__(self, matrix=None):
        """ matrix will be a 2 dimentional array of cells"""
        if matrix is None:
            self._matrix = []
        else:
            self._matrix = matrix
        self._max_y = len(self._matrix) - 1
        if self._matrix:
            self._max_x = len(self._matrix[0]) - 1
        else:
            self._max_x = -1

    def get_cell_at(self, x, y):
        return self._matrix[y][x]

    def get_cells_around(self, cell):
        x, y = cell.get_location()
        return_list=[]
        for i in xrange(max(0, x-1), min(x+1, self._max_x)+1):
            for j in xrange(max(0, y-1), min(y+1, self._max_y)+1):
                if not (i, j) == (x, y):
                    return_list.append(self._matrix[j][i])
        return return_list

    def evaluate(self):
        new_matrix = []
        for row in self._matrix:
            new_row = []
            for c in row:
                new_row.append(c.evaluate_next(self))
            new_matrix.append(new_row)
        return Grid(new_matrix)

    def is_live(self):
        for row in self._matrix:
            for cell in row:
                if cell.is_live():
                    return True
        return False

    def __repr__(self):
        #outstr='(max_x, max_y) = ({}, {})\n'.format(self._max_x, self._max_y)
        outstr=''
        for row in self._matrix:
            for c in row:
                outstr +=( 'x' if c.is_live() else ' ' )
            outstr += '\n'
        return outstr[:-1]

    @classmethod
    def from_str(clazz, string):
        y = -1
        matrix = []
        grid = clazz()
        for row in string.split('\n'):
            y += 1
            x = -1
            grid_row = []
            for c in row:
                x += 1
                grid_row.append(GridCell(x, y, c == 'x'))
            matrix.append(grid_row)
        grid._matrix = matrix
        grid._max_x = x
        grid._max_y = y
        return grid

if __name__ == '__main__':
    grid_str = "    x   " + '\n' + \
               " xxxx   " + '\n' + \
               " xxxx   " + '\n' + \
               " xxxx   " + '\n' + \
               " xxxx   " + '\n' + \
               "  x     " + '\n' + \
               "        "

    grid = Grid.from_str(grid_str)
    while grid.is_live():
        os.system('clear')
        grid = grid.evaluate()
        print grid
        import time 
        time.sleep(1)


#--------------------------------------------------------------------------------

from mock import MagicMock

grid = Grid()
live_cell = GridCell(live=True)
dead_cell = GridCell(live=False)

def test_setup():
    cell = GridCell(3, 2)
    assert cell.get_location() == (3, 2)
    assert cell.is_live() == False

def test_when_dead_less_three_live_neighbours_should_give_birth():
    cell = GridCell()
    grid.get_cells_around = MagicMock(return_value = (3*[live_cell]+4*[dead_cell]))
    assert cell.evaluate_next(grid).is_live()

def test_when_dead_less_greater_then_3_should_leave_it_dead():
    cell = GridCell(grid)
    grid.get_cells_around = MagicMock(return_value = (4*[live_cell]+4*[dead_cell]))
    assert cell.evaluate_next(grid).is_live() == False
    
def test_when_dead_less_then_3_should_leave_it_dead():
    cell = GridCell(grid)
    grid.get_cells_around = MagicMock(return_value = (2*[live_cell]+4*[dead_cell]))
    assert cell.evaluate_next(grid).is_live() == False

def test_when_alive_greater_than_3_should_leave_it_dead():
    cell = GridCell(grid, live=True)
    grid.get_cells_around = MagicMock(return_value = (4*[live_cell]+4*[dead_cell]))
    assert cell.evaluate_next(grid).is_live() == False

def test_when_alive_less_than_2_should_leave_it_dead():
    cell = GridCell(grid, live=True)
    grid.get_cells_around = MagicMock(return_value = (1*[live_cell]+4*[dead_cell]))
    assert cell.evaluate_next(grid).is_live() == False

def test_when_alive_2_or_3_should_leave_it_alive():
    cell = GridCell(grid, live=True)
    grid.get_cells_around = MagicMock(return_value = (2*[live_cell]+4*[dead_cell]))
    assert cell.evaluate_next(grid).is_live() 
    cell = GridCell(grid, live=True)
    grid.get_cells_around = MagicMock(return_value = (3*[live_cell]+4*[dead_cell]))
    assert cell.evaluate_next(grid).is_live() 

def cell_test(grid, x, y, neighbours_location, live=True):
    cell = grid.get_cell_at(x, y)
    assert cell.get_location() == (x, y)
    assert cell.is_live() == live
    neighbours = grid.get_cells_around(cell)
    assert len(neighbours) == len(neighbours_location)
    locations = [x.get_location() for x in neighbours]
    for l in neighbours_location:
        assert l in locations

def test_grid_setup():
    string='x x\n x \nx x'
    grid = Grid.from_str(string)

    cell_test(grid, x=0, y=0, neighbours_location=[(0, 1), (1, 0), (1, 1)])
    cell_test(grid, x=1, y=0, neighbours_location=[(0, 0), (0, 1), (1, 1), (2, 0), (2, 1)], live=False)

    string='   \nxxx\n   '
    grid = Grid.from_str(string)

    cell_test(grid, x=0, y=0, neighbours_location=[(0, 1), (1, 0), (1, 1)], live=False)


def test_horizontal():
    string='   \nxxx\n   '
    grid = Grid.from_str(string)
    next_grid = grid.evaluate()
    assert next_grid.__repr__() == ' x \n x \n x '

    next_grid1 = next_grid.evaluate()
    assert next_grid1.__repr__() == '   \nxxx\n   '

