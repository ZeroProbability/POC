#!/usr/bin/env python
# encoding: utf-8

def read_test_cases():
    number_of_tests=int(raw_input())
    for _ in xrange(number_of_tests):
        number_of_rows=int(raw_input())
        rows=[]
        for i in number_of_rows:
            row=[int(n) for n in raw_input().split()]
            rows.append(row)
        yield rows

def main():
    print read_test_cases()
    print "Hello there"

if __name__ == '__main__':
    main()

#------------------------------------------------------------------------

def test_something():
    assert 1 == 2
