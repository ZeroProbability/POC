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

def isvalid(grid, n):
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

def arrange(n, m, ):
    pass

def parse_input_grid(n, size, data_row):
    grid = []
    for row in xrange(n):
        grid.append([E] * n)

    return grid

def print_grid(grid):
    for row in xrange(len(grid)):
        print ''.join(grid[row])

#------------------------------------------------------------------------

def test_valid():
    grid = parse_input_grid(3, 0, [])
    print_grid(grid)
    assert 1 == 2

