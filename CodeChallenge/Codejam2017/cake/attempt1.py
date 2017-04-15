#!/usr/bin/env python
# encoding: utf-8

def solve(grid):
    r = len(grid)
    c = len(grid[0])
    sgrid = []
    for ri in xrange(r):
        row = ['?'] * c
        sgrid.append(row)

    print grid
    print sgrid
    for ri in xrange(r):
        for ci in xrange(c):
            if grid[ri][ci] == '?':
                continue
            ris, rie = ri, ri
            cis, cie = ci, ci
            while(ris >= 0):
                ris = max(ris-1, 0)
                if grid[ris] == '?':
                    break

            while(rie < r and grid[rie] == '?'):
                print "here 2"
                rie = min(r-1, rie + 1)
            print ris, rie


def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        r, c = raw_input().split(" ")
        r, c = int(r), int(c)
        grid = []
        for ri in xrange(r):
            cs = raw_input()
            grid.append(list(cs)) 
            solve(grid)

if __name__ == '__main__':
    main()

#------------------------------------------------------------------------

def test_find_untidy_digit():
    grid = [list('G??'),
            list('?C?'),
            list('??J')
            ]
    print solve(grid)
    assert 1 == 2
