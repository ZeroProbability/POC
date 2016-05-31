#!/usr/bin/env python
# encoding: utf-8

def read_test_cases():
    number_of_tests=int(raw_input())
    for _ in xrange(number_of_tests):
        number_of_rows=int(raw_input())
        rows=[]
        for i in xrange(number_of_rows):
            row=[int(n) for n in raw_input().split()]
            rows.append(row)
        yield rows

def evaluate(case):
    case = case[::-1]
    sums = []
    sum_row = case[0]
    sums.append(sum_row)
    for row in case[1:]:
        new_row=[]
        for i, n in enumerate(row):
            new_row.append(n + max(sum_row[i] , sum_row[i+1]))
        sums.append(new_row)
        sum_row = new_row
    return sums[::-1]

def main():
    for case in read_test_cases():
        print evaluate(case)[0][0]

if __name__ == '__main__':
    main()

#------------------------------------------------------------------------

def test_something():
    case1 = [ [1], [10, 20], [100, 200, 300] ]
    assert evaluate(case1) == [ [321], [210, 320], [100, 200, 300]]

