#!/usr/bin/env python
# encoding: utf-8

import copy

O, X, P, E = 'o', 'x', '+', '.'

def isvalid(grid):
    n = len(grid)
    for row in xrange(n):
        o_count = 0
        for col in xrange(n):
            if grid[row][col] in [O, X]:
                o_count += 1
            if o_count > 1: return False

    for col in xrange(n):
        o_count = 0
        for row in xrange(n):
            if grid[row][col] in [O, X]:
                o_count += 1
            if o_count > 1: return False

    o_count = 0
    for row in xrange(n):
        if grid[row][row] in [O, P]:
            o_count += 1
        if o_count > 1: return False

    o_count = 0
    for row in xrange(n):
        if grid[row][n - row - 1] in [O, P]:
            o_count += 1
        if o_count > 1: return False

    return True

def arrange(grid):
    grid = copy.deepcopy(grid)
    assign_max(grid)
    n = len(grid)
    for row in xrange(n):
        for col in xrange(n):
            if grid[row][col] in [X, P]:
                new_grid = copy.deepcopy(grid)
                new_grid[row][col] = O
                if isvalid(new_grid):
                    arrange(new_grid)
            if grid[row][col] == E:
                new_grid = copy.deepcopy(grid)
                new_grid[row][col] = X
                if isvalid(new_grid):
                    arrange(new_grid)
                new_grid[row][col] = P
                if isvalid(new_grid):
                    arrange(new_grid)
                new_grid[row][col] = O
                if isvalid(new_grid):
                    arrange(new_grid)


max_grid = None
max_score = 0
def assign_max(grid):
    global max_grid, max_score
    ts = score(grid)
    if ts > max_score:
        max_grid = copy.deepcopy(grid)
        max_score = ts

def score(grid):
    n = len(grid)
    s = 0
    for row in xrange(n):
        for col in xrange(n):
            if grid[row][col] in [X, P]:
                s += 1
            if grid[row][col] == O:
                s += 2

    return s

#O, X, P, E = 'o', 'x', '+', '.'
def parse_input_grid(n, data_row):
    grid = []
    for row in xrange(n):
        grid.append([E] * n)

    for i in xrange(len(data_row)):
        d, r, c = data_row[i].split(' ')
        r = int(r) - 1
        c = int(c) - 1
        ix = [O, X, P, E].index(d)
        d = [O, X, P, E][ix]
        grid[r][c] = d

    return grid

def print_grid(grid):
    for row in xrange(len(grid)):
        print ''.join(grid[row])

def print_diff(in_grid, out_grid):
    n = len(in_grid)
    res = []
    for row in xrange(n):
        for col in xrange(n):
            if out_grid[row][col] != in_grid[row][col]:
                res.append("{} {} {}".format(out_grid[row][col], row+1, col+1))

    return res

def main():
    t = int(raw_input())
    global max_score, max_grid
    for i in xrange(t):
        n, m = raw_input().split(" ")
        n, m = int(n), int(m)
        rows = []
        for r in xrange(m):
            rows.append(raw_input())
        grid = parse_input_grid(n, rows)
        max_score, max_grid = score(grid), grid
        arrange(grid)
        res = print_diff(grid, max_grid)
        print "Case #{}: {} {}".format(i+1, max_score, len(res))
    print_grid(max_grid)

if __name__ == '__main__':
    main()

#------------------------------------------------------------------------

def test_valid_o1():
    grid = parse_input_grid(3, ['o 1 1', 'x 2 1', '+ 3 3'])
    print_grid(grid)
    assert not isvalid(grid)

def test_valid_o2():
    grid = parse_input_grid(3, ['o 1 1', 'o 2 1', '+ 3 3'])
    print_grid(grid)
    assert not isvalid(grid)

def test_valid_o3():
    grid = parse_input_grid(3, ['o 1 1', 'o 1 2', '+ 3 3'])
    print_grid(grid)
    assert not isvalid(grid)

def test_valid_o4():
    grid = parse_input_grid(3, ['o 1 1', 'o 2 2', '+ 3 3'])
    print_grid(grid)
    assert not isvalid(grid)

def test_valid_o5():
    grid = parse_input_grid(3, ['o 1 3', 'o 2 2', '+ 3 3'])
    print_grid(grid)
    assert not isvalid(grid)

def test_valid_x1():
    grid = parse_input_grid(3, ['x 1 1', 'x 1 2', '+ 3 3'])
    print_grid(grid)
    assert not isvalid(grid)

def test_valid_x2():
    grid = parse_input_grid(3, ['x 1 1', 'x 2 1', '+ 3 3'])
    print_grid(grid)
    assert not isvalid(grid)

def test_valid_p1():
    grid = parse_input_grid(3, ['+ 1 1', 'x 2 2', '+ 3 3'])
    print_grid(grid)
    assert not isvalid(grid)

def test_valid_cx():
    grid = parse_input_grid(2, ['o 1 1', 'x 1 2', 'x 2 1', 'o 2 2'])
    print_grid(grid)
    assert not isvalid(grid)

def test_s1():
    global max_grid, max_score

    max_score = 0
    grid = parse_input_grid(2, [])
    arrange(grid)
    print_grid(max_grid)
    assert max_score == 4

def test_s2():
    global max_grid, max_score

    max_score = 0
    grid = parse_input_grid(1, ['o 1 1'])
    arrange(grid)
    print_grid(max_grid)
    assert max_score == 2

def test_s3():
    global max_grid, max_score

    max_score = 0
    grid = parse_input_grid(3, ['+ 2 3', '+ 2 1', 'x 3 1', '+ 2 2'])
    arrange(grid)
    print print_diff(grid, max_grid)
    assert max_score == 8

