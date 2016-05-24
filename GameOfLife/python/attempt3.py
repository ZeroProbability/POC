#!/usr/bin/env python
# encoding: utf-8

class Grid(object):

    def __init__(self, xlen, ylen):
        self._xlen = xlen
        self._ylen = ylen

    def init_random_grid(self):
        for y in xrange(0, self._ylen):
            new_row = [x for x in xrange(0, self._xlen)]


