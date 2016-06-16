#!/usr/bin/env python
# encoding: utf-8

def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'
    elif n % 3 == 0:
        return 'Fizz'
    elif n % 5 == 0:
        return 'Buzz'
    return None

def main():
    for i in xrange(1, 100):
        fb = fizzbuzz(i)
        if fb:
            yield i, fb

if __name__ == '__main__':
    for x,y in main():
        print x,y

#------------------------------------------------------------------------

def test_fizzbuzz():
    assert fizzbuzz(3) == 'Fizz'
    assert fizzbuzz(5) == 'Buzz'
    assert fizzbuzz(15) == 'FizzBuzz'
    assert fizzbuzz(10) == 'Buzz'
    assert fizzbuzz(9) == 'Fizz'
    assert fizzbuzz(8) is None

