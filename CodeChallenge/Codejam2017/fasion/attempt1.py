#!/usr/bin/env python
# encoding: utf-8

O, X, P, E = 'o', 'x', '+', '.'

def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        n, k = (int(x) for x in raw_input().split(" "))
        l = [MaxHeapObj(n)]
        split_n_times(l, k-1)

        if len(l) == 0:
            print "Case #{}: 0 0".format(i)
        else:
            m = heapq.heappop(l).val
            if m % 2 == 0:
                #even 
                print "Case #{}: {} {}".format(i, (m-1)/2 + 1, (m-1)/2)
            else:
                print "Case #{}: {} {}".format(i, (m-1)/2, (m-1)/2)

if __name__ == '__main__':
    main()

def isvalid(grid):
    n = len(grid)
    for row in xrange(n):
        o_count = 0
        for col in xrange(n):
            if grid[row][col] == O:
                o_count += 1
            if o_count > 1: return False

    for col in xrange(n):
        o_count = 0
        for row in xrange(n):
            if grid[row][col] == O:
                o_count += 1
            if o_count > 1: return False

    for row in xrange(n):
        o_count = 0
        if grid[row][row] == O:
            o_count += 1

    for row in xrange(n):
        x_count = 0
        for col in xrange(n):
            if grid[row][col] == X:
                x_count += 1
            if x_count > 1: return False

    for col in xrange(n):
        x_count = 0
        for row in xrange(n):
            if grid[row][col] == X:
                x_count += 1
            if x_count > 1: return False

    return True

def arrange(n, m, ):
    pass

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

#------------------------------------------------------------------------

def test_valid_o1():
    grid = parse_input_grid(3, ['o 1 1', 'x 2 1', '+ 3 3'])
    print grid
    assert isvalid(grid)

def test_valid_o2():
    grid = parse_input_grid(3, ['o 1 1', 'o 2 1', '+ 3 3'])
    print grid
    assert not isvalid(grid)

def test_valid_o3():
    grid = parse_input_grid(3, ['o 1 1', 'o 1 2', '+ 3 3'])
    print grid
    assert not isvalid(grid)

def test_valid_x1():
    grid = parse_input_grid(3, ['x 1 1', 'x 1 2', '+ 3 3'])
    print grid
    assert not isvalid(grid)

def test_valid_x2():
    grid = parse_input_grid(3, ['x 1 1', 'x 2 1', '+ 3 3'])
    print grid
    assert not isvalid(grid)
