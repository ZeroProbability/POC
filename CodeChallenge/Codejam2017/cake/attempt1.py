#!/usr/bin/env python
# encoding: utf-8

def solve(grid):
    r = len(grid)
    for ri in xrange(r):
        print ri

def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        r, c = raw_input().split(" ")
        r, c = int(r), int(c)
        grid = []
        for ri in xrange(r):
            cs = raw_input()
            grid += list(cs)
            solve(grid)

if __name__ == '__main__':
    main()

#------------------------------------------------------------------------

def test_find_untidy_digit():
    grid = [list('G??'),
            list('?C?'),
            list('??J')
            ]
    assert 1 == 2
