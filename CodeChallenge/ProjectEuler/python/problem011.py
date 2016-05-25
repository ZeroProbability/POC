#!/usr/bin/env python
# encoding: utf-8


matrix = [
        " 1  2  3  4  5".split(),
        "11 12 13 14 15".split(),
        "21 22 23 24 25".split(),
        "31 32 33 34 35".split(),
        "41 42 43 44 45".split()
        ]

def read_horizontals(length):
    for y in xrange(len(matrix)):
        for x in xrange(len(matrix[0]) - length + 1):
            yield map(int, matrix[y][x:(x + length)])

def read_verticals(length):
    for x in xrange(len(matrix[0])):
        for y in xrange(len(matrix)-length + 1):
            yield map(int, [ matrix[y+i][x] for i in xrange(length) ])

def read_diagnols(length):
    for x in xrange(len(matrix[0])):
        for y in xrange(len(matrix)-length + 1):
            yield map(int, [ matrix[y+i][x] for i in xrange(length) ])

if __name__ == '__main__':
    print "blah"


#-------------------------------------------------------------------------------

def test_something():
    assert list(read_horizontals(2))[0]  == [ 1, 2 ]
    assert list(read_horizontals(2))[3]  == [ 4, 5 ]
    assert list(read_horizontals(2))[4]  == [ 11, 12 ]
    assert list(read_horizontals(2))[-1]  == [ 44, 45 ]

    assert list(read_verticals(2))[0]  == [ 1, 11 ]
    assert list(read_verticals(2))[3]  == [ 31, 41 ]
    assert list(read_verticals(2))[4]  == [ 2, 12 ]
    assert list(read_verticals(2))[-1]  == [ 35, 45 ]


