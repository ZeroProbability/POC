#!/usr/bin/env python
# encoding: utf-8


matrix = [
        " 1  2  3  4  5".split(),
        "11 12 13 14 15".split(),
        "21 22 23 24 25".split(),
        "31 32 33 34 35".split(),
        "99 42 43 44 45".split()
        ]

for i in xrange(20):
    matrix = []
    matrix += raw_input().split()

def read_horizontals(length):
    for y in xrange(len(matrix)):
        for x in xrange(len(matrix[0]) - length + 1):
            yield map(int, matrix[y][x:(x + length)])

def read_verticals(length):
    for x in xrange(len(matrix[0])):
        for y in xrange(len(matrix)-length + 1):
            yield map(int, [ matrix[y+i][x] for i in xrange(length) ])

def read_diagnols1(length):
    for y in xrange(len(matrix) - length + 1):
        for x in xrange(len(matrix[0]) - length + 1):
            yield map(int, [ matrix[y+i][x+i] for i in xrange(length) ])

def read_diagnols2(length):
    for y in xrange(len(matrix) - length + 1):
        for x in xrange(length - 1, len(matrix[0])):
            yield map(int, [ matrix[y+i][x-i] for i in xrange(length) ])

def all_of_it(length):
    for i in read_horizontals(length):
        yield i
    for i in read_verticals(length):
        yield i
    for i in read_diagnols1(length):
        yield i
    for i in read_diagnols2(length):
        yield i

def all_products(length):
    for i in all_of_it(length):
        yield reduce(lambda acc, x: acc * x, i, 1)

if __name__ == '__main__':
    print max(all_products(2))


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

    assert list(read_diagnols1(2))[0]  == [ 1, 12 ]
    assert list(read_diagnols1(2))[3]  == [ 4, 15]
    assert list(read_diagnols1(2))[-1]  == [ 34, 45]

    assert list(read_diagnols2(2))[0]  == [ 2, 11 ]
    assert list(read_diagnols2(2))[3]  == [ 5, 14 ]
    assert list(read_diagnols2(2))[-1]  == [ 35, 44 ]

