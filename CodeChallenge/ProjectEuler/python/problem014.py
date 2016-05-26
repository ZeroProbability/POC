import functools
import itertools
import array

cache = array.array('L', [0] * 200000000)
cache[1] = 1

max_len_cache = array.array('L', [0] * 20000000)
last_populated = 1
max_len_cache[1] =  1 # len 

def read_test_cases():
    number_of_tests=int(raw_input())
    for _ in xrange(number_of_tests):
        yield int(raw_input())

def f(n):
    if n % 2 == 0:
        return n/2
    return 3 * n + 1

def len_chain_f(n):
    if cache[n]:
        return cache[n]
    next_n = f(n)
    if cache[next_n]:
        cache[n] = 1 + cache[next_n]
        return cache[n]
    return 1 + len_chain_f(f(n))

def max_len_under(n):
    global last_populated
    if max_len_cache[n]:
        return max_len_cache[n]
    max_in_cache = last_populated
    for i in xrange(max_in_cache+1, n+1):
        if len_chain_f(i) >= max_len_cache[i-1]:
            max_len_cache[i] = len_chain_f(i)
        else:
            max_len_cache[i] = max_len_cache[i-1]

    last_populated = n
    return max_len_cache[n]

def main():
    for c in read_test_cases():
        print max_len_under(c)

if __name__ == '__main__':
    main()

