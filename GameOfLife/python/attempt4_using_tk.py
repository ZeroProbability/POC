#!/usr/bin/env python
# encoding: utf-8

from tkinter import *
from itertools import product


def neighbors(y, x):
    return set(product([y-1, y, y+1], [x-1, x, x+1])) - set([(y,x)])
    

class Grid(object):

    def __init__(self):
        self._grid = []

    @classmethod
    def init_from(clazz, two_d_array):
        ylen = len(two_d_array)
        xlen = len(two_d_array[0])

        grid = set()
        for x in xrange(xlen):
            for y in xrange(ylen):
                if two_d_array[y][x]:
                   grid.add((y,x))

        return grid




#        master = Tk()
# 
#        w = Canvas(master, width=200, height=100)
#        w.pack()
# 
#        w.create_rectangle(50, 20, 150, 80, fill="#476042")
# 
#        mainloop()


#-------------------------------------------------------------------------------

def test_grid_cast1():
    test_grid = [[ 0, 0, 0, 0  ], 
                 [ 0, 1, 1, 0  ], 
                 [ 0, 1, 1, 0  ], 
                 [ 0, 1, 1, 0  ], 
                 [ 0, 0, 0, 0  ]] 

    grid = Grid.init_from(test_grid)

    print grid

    print neighbors(3, 2)

    assert 1 == 2
