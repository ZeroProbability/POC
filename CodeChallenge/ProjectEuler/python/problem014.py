import functools
import itertools

cache = [None] * 5000000
cache[1] = 1

max_len_cache = [None] * 5000000  # preallocate
last_populated = 1
max_len_cache[1] = ( 1, 1) # len , at

def read_test_cases():
    number_of_tests=int(raw_input())
    for _ in xrange(number_of_tests):
        yield int(raw_input())

def f(n):
    if n % 2 == 0:
        return n/2
    return 3 * n + 1

def len_chain_f(n):
    if n < 5000000 and cache[n]:
        return cache[n]
    next_n = f(n)
    if n < 5000000 and next_n < 5000000 and cache[next_n]:
        cache[n] = 1 + cache[next_n]
        return cache[n]
    return 1 + len_chain_f(f(n))

def max_len_under(n):
    global last_populated
    if max_len_cache[n]:
        return max_len_cache[n]
    max_in_cache = last_populated
    for i in xrange(max_in_cache+1, n+1):
        if len_chain_f(i) >= max_len_cache[i-1][0]:
            max_len_cache[i] = ( len_chain_f(i), i)
        else:
            max_len_cache[i] = max_len_cache[i-1]

    last_populated = n
    return max_len_cache[n]

def main():
    for c in read_test_cases():
        print max_len_under(c)[1]

if __name__ == '__main__':
    main()

