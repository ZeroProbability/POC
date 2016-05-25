#!/usr/bin/env python
# encoding: utf-8

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    upto=int(math.floor(math.sqrt(n))+1)
    for i in xrange(2, upto):
        if n % i == 0:
            return False
    return True


def primes_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

    return a


def read_test_cases():
    number_of_tests=int(raw_input())
    test_cases=[int(raw_input()) for x in xrange(number_of_tests)]
    return test_cases

def main():
    ps = primes_sieve(1000000)
    result = []
    for i, p in enumerate(ps):
        if p:
            result.append(i)

    for tc in read_test_cases():
        print result[tc-1]

if __name__ == '__main__':
    main()
