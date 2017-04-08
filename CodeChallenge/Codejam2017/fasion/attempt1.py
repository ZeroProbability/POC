#!/usr/bin/env python
# encoding: utf-8

import heapq

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

def arrange():

#------------------------------------------------------------------------

def test_arrage():

