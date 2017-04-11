#!/usr/bin/env python
# encoding: utf-8

def solve(n, m):
    return {'sum': n + m ,'product': n * m}

def print_result(testcase_index, **kwargs):
    print "Case #{}: {sum} {product}".format(testcase_index, **kwargs)

def run_tests(input_lines):
    ''' yields one test case at a time ''' 
    t = int(input_lines[0])
    for i in xrange(1, t + 1):
        input_line = raw_input()
        n, m = [int(s) for s in input_line.split(" ")] 
        solution = solve(n = n, m = m)
        print_result(i, **solution)

if __name__ == '__main__':
    run_tests()

# ------------------------------------------------------------------------------

def test_solve():
    assert solve(3, 4) == { 'sum': 7, 'product': 12 }
