import functools
import itertools

cache = {1: 1}

max_len_cache = {1: {'len': 1, 'at': 1}}

def read_test_cases():
    number_of_tests=int(raw_input())
    for _ in xrange(number_of_tests):
        yield int(raw_input())

def f(n):
    if n % 2 == 0:
        return n/2
    return 3 * n + 1

def len_chain_f(n):
    if cache.get(n):
        return cache[n]
    next_n = f(n)
    if cache.get(next_n):
        cache[n] = 1 + cache[next_n]
        return cache[n]
    return 1 + len_chain_f(f(n))

def max_len_under(n):
    if max_len_cache.get(n):
        return max_len_cache[n]['at']
    max_in_cache = max(max_len_cache.keys())
    for i in xrange(max_in_cache+1, n+1):
        if len_chain_f(i) >= max_len_cache[i-1]['len']:
            max_len_cache[i] = {'len': len_chain_f(i), 'at': i}
        else:
            max_len_cache[i] = max_len_cache[i-1]

    return max_len_cache[n]

def main():
    for c in read_test_cases():
        print max_len_under(c)['at']

if __name__ == '__main__':
    main()

