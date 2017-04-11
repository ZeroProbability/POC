#!/usr/bin/env python
# encoding: utf-8

import sys

def solve(i, search_engines, queries):
    engs = set(search_engines)
    switch_count = 0
    for q in queries:
        if q in engs:
            engs.remove(q)
            if len(engs) == 0:
                switch_count += 1
                engs = set(search_engines)
                engs.remove(q)

    return "Case #{}: {}".format(i, switch_count)

def run_tests(lines):
    def next_line():
        next_line.line_no += 1
        return lines[next_line.line_no]

    next_line.line_no = 0

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
    assert solve(1, ['google', 'yahoo'], ['yahoo', 'google']) == "Case #1: 1"
    assert solve(1, ['google', 'yahoo'], ['yahoo', 'google', 'google', 'yahoo']) == "Case #1: 2"

def test_sample():
    input_data = """2
5
Yeehaw
NSM
Dont Ask
B9
Googol
10
Yeehaw
Yeehaw
Googol
B9
Googol
NSM
B9
NSM
Dont Ask
Googol
5
Yeehaw
NSM
Dont Ask
B9
Googol
7
Googol
Dont Ask
NSM
NSM
Yeehaw
Yeehaw
Googol
    """.splitlines()
    expected_output = """Case #1: 1
Case #2: 0"""
    assert "\n".join(list(run_tests(input_data))) == expected_output
