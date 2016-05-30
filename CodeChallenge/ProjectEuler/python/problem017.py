#!/usr/bin/env python
# encoding: utf-8

to_twenty= ['', 'One' , 'Two' , 'Three' , 'Four' , 'Five' , 'Six' , 'Seven' , 'Eight' , 'Nine' , 'Ten' ,
         'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Ninteeen', 'Twenty']

tens = [ '', 'Ten', 'Twenty', 'Thirty', 'Fourty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninghty', 'Hundred']

def handle_to_thousand(i):
    h = i // 100
    r = i % 100
    if r < 20:
        rs = to_twenty[r]
    else:
        if r//10 > 0:
            return ' '.join(tens[r//10], 'Hundred', to_twenty(r%10))
    return ' '.join([handle_to_20(h), rs])

def split_into_thousands(n):
    yield n % 1000
    while n // 1000 > 0:
        n = n // 1000
        yield n % 1000

def main():
    for c in split_into_thousands(10334342343):
        print c


if __name__ == '__main__':
    main()
