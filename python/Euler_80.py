#!/usr/bin/python
from decimal import *

if __name__ == '__main__':
    getcontext().prec = 150
    total = 0

    for i in range(100):
        if i**0.5 != int(i**0.5):
            sqrt_s = ''.join(str(Decimal(i).sqrt()).split('.'))[:100]
            digits = map(int, list(sqrt_s))
            total += sum(digits)

    print 'Total: %s' % total