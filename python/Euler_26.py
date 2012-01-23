from decimal import *

getcontext().prec = 5000

_max = 0
_maxd = 0

for d in range(7, 1000):
    end = str(1 / Decimal(d))[10:]
    f = end[:12]
    i1 = end.find(f)
    i2 = end.find(f,i1+1)
    i3 = end.find(f,i2+1)
    i4 = end.find(f,i3+1)
    i5 = end.find(f,i4+1)

    if i5 - i4 == i4 - i3 == i3 - i2 == i2 - i1:
        if i5 - i4 > _max:
            _max = i5 - i4
            _maxd = d
        print '%s: %s' % (d, i4 - i3)

print 'Max: %s with %s digits' % (_maxd, _max)
