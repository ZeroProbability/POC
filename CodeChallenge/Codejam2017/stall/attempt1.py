#!/usr/bin/env python
# encoding: utf-8

from numba import jit
import heapq

class MaxHeapObj(object):
  def __init__(self,val): self.val = val
  def __lt__(self,other): return self.val > other.val
  def __eq__(self,other): 
      if type(other) == MaxHeapObj:
          return self.val == other.val
      return self.val == other
  def __str__(self): return str(self.val)

def main():
    t = int(raw_input())
    for i in xrange(1, t + 1):
        s = int(raw_input())
        print "Case #{}: {}".format(i, prevtidy(s))

def split_list(l):
    m = heapq.heappop(l)
    if m.val == 1:
        pass # nothing to push back
    elif m.val == 2:
        heapq.heappush(l, MaxHeapObj(1))
    elif (m.val - 1) % 2 == 0:
        # odd case - can be split equally
        heapq.heappush(l, MaxHeapObj((m.val - 1) / 2))
        heapq.heappush(l, MaxHeapObj((m.val - 1) / 2))
    else:
        # even case - unevenly split
        heapq.heappush(l, MaxHeapObj((m.val - 1) / 2))
        heapq.heappush(l, MaxHeapObj((m.val - 1) / 2 + 1))

if __name__ == '__main__':
    main()

#------------------------------------------------------------------------

def test_split():
    l = [MaxHeapObj(4)]
    heapq.heapify(l)
    split_list(l)
    assert sorted([i.val for i in l]) == [1, 2]
    split_list(l)
    assert sorted([i.val for i in l]) == [1, 1]
    split_list(l)
    assert sorted([i.val for i in l]) == [1]
    split_list(l)
    assert sorted([i.val for i in l]) == []

    l = [MaxHeapObj(5)]
    heapq.heapify(l)
    split_list(l)
    assert sorted([i.val for i in l]) == [2, 2]
    split_list(l)
    assert sorted([i.val for i in l]) == [1, 2]

    l = [MaxHeapObj(6)]
    heapq.heapify(l)
    split_list(l)
    assert sorted([i.val for i in l]) == [2, 3]
    split_list(l)
    assert sorted([i.val for i in l]) == [1, 1, 2]
    split_list(l)
    assert sorted([i.val for i in l]) == [1, 1, 1]
    split_list(l)
    assert sorted([i.val for i in l]) == [1, 1]

    l = [MaxHeapObj(1000)]
    heapq.heapify(l)
    split_list(l)
    assert sorted([i.val for i in l]) == [499, 500]

    l = [MaxHeapObj(1000000)]
    heapq.heapify(l)
    for i in xrange(1000000):
        split_list(l)
    assert sorted([i.val for i in l]) == []

