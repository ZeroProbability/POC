#!/usr/bin/env python
# encoding: utf-8

import sys

def solve(i, n, m):
    return "Case #{}: {} {}".format(i, n + m , n * m)

def run_tests(lines):
    t = int(lines[0])
    for i in xrange(1, t + 1):
        input_line = lines[i]
        n, m = [int(s) for s in input_line.split(" ")] 
        solution = solve(i, n, m)
        yield solution

if __name__ == '__main__':
    with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
        lines = f.read().splitlines()
        for l in run_tests(lines):
            print l

# ------------------------------------------------------------------------------

def test_solve():
    assert solve(1, 3, 4) == "Case #1: 7 12"

def test_sample():
    input_data = """2
3 4
4 5
""".splitlines()
    expected_output = """Case #1: 7 12
Case #2: 9 20"""
    assert "\n".join(list(run_tests(input_data))) == expected_output
