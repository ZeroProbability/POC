#!/usr/bin/env python
# encoding: utf-8

import itertools

capacity = 10

weights = [1, 3, 4, 7, 9]
benefit = [3, 2, 5, 4, 3]

def possibilities():
    for itemcount in xrange(1, len(weights)+1):
        for i in itertools.combinations(xrange(len(weights)), itemcount):
            yield i

def filter_capacity(indexes):
    cal_capacity = sum(weights[i] for i in indexes)
    return cal_capacity <= capacity

def sum_benefit(indexes):
    benefit_sum = sum(benefit[i] for i in indexes)
    return benefit_sum, tuple(weights[i] for i in indexes) 

def main():
    dd = itertools.ifilter(filter_capacity, possibilities())
    ff = itertools.imap(sum_benefit, dd)
    print max(ff)

if __name__ == '__main__':
    main()
