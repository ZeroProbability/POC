#!/usr/bin/env python
# encoding: utf-8

to_twenty= ['', 'One' , 'Two' , 'Three' , 'Four' , 'Five' , 'Six' , 'Seven' , 'Eight' , 'Nine' , 'Ten' ,
         'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Ninteeen', 'Twenty']

tens = [ '', 'Ten', 'Twenty', 'Thirty', 'Fourty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'Hundred']

bigs = ['', 'Thousand', 'Million', 'Billion', 'Trillion']

def handle_to_hundred(i):
    if i < 20:
        return to_twenty[i%20]
    else:
        return ' '.join([tens[i//10], to_twenty[i%10]])

def handle_to_thousand(i):
    if i < 100:
        return handle_to_hundred(i)
    else:
        return ' '.join([to_twenty[i//100], 'Hundred', handle_to_hundred(i%100)])


def split_into_thousands(n):
    yield n % 1000
    while n // 1000 > 0:
        n = n // 1000
        yield n % 1000


def read_test_cases():
    number_of_tests=int(raw_input())
    for _ in xrange(number_of_tests):
        yield int(raw_input())

def main():
    for tcase in read_test_cases():
        if tcase == 0:
            print 'Zero'
        else:
            tbigs = bigs[:]
            next_suffix = tbigs.pop(0)
            r = []
            for c in split_into_thousands(tcase):
                r.insert(' '.join([c, handle_to_thousand(c), next_suffix]))
                next_suffix = tbigs.pop(0)
            print ' '.join(r)


if __name__ == '__main__':
    main()
