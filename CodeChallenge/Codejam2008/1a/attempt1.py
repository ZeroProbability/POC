#!/usr/bin/env python
# encoding: utf-8

import sys

def solve(i, search_engines, queries):
    engs = set(search_engines)
    for q in queries:
    return "Case #{}: {} {}".format(i, n + m , n * m)

def run_tests(lines):
    line_no = 1
    def next_line():
        line_no += 1
        return lines[line_no]

    t = int(lines[0])
    for i in xrange(1, t + 1):
        search_engine_count = int(next_line())
        search_engines = []
        for j in xrange(search_engine_count):
            search_engines.append(next_line())

        query_count = int(next_line())
        queries = []
        for j in xrange(query_count):
            queries.append(next_line())

        solution = solve(i, search_engines, queries)
        yield solution

if __name__ == '__main__':
    with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
        lines = f.read().splitlines()
        for l in run_tests(lines):
            print l

# ------------------------------------------------------------------------------

def test_solve():
    assert solve(1, ['google', 'yahoo'], ['yahoo', 'xyz']) == "Case #1: 0"

def _test_sample():
    input_data = """2
3 4
4 5
""".splitlines()
    expected_output = """Case #1: 7 12
Case #2: 9 20"""
    assert "\n".join(list(run_tests(input_data))) == expected_output
