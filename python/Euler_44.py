from math import sqrt

def ispent(n):
    p = (1 + sqrt(1 + 24 * n)) / 6.0
    return p == int(p)

def pent(n):
    return n * (3 * n - 1) / 2

_min = 1000000000000000

for c in range(1,5000):
    for i in range(1,c):
        if ispent(pent(c) + pent(i)) and ispent(pent(c) - pent(i)):
            d = pent(c) - pent(i)
            print 'Success! %s' % d
            if d < _min:
                _min = d

print _min
    
