#!/usr/bin/env python
# encoding: utf-8

from tkinter import *


class Grid(object):

    def __init__(self, lenx=0, leny=0):
        self._lenx = lenx
        self._leny = leny

        self._grid = []

    @classmethod
    def init_from(clazz, two_d_array):
        leny = len(two_d_array)
        if leny:
            lenx = len(two_d_array[0])
        else:
            lenx = 0
        
        inst=clazz(lenx, leny)
        inst._grid = two_d_array

        return inst

    def as_two_d_array(self):
        return self._grid[:]


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

    grid = Grid.init_from(test_grid).as_two_d_array()

    print grid

    assert 1 == 2
