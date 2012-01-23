from math import *

def factorsum(n):
    t = 1
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            t += i
            if i**2 <> n:
                t += n/i
    return t

total = 0
a,b = 0,0

for i in range(4,10000):
    a = factorsum(i)
    b = factorsum(a)
    if i == b and a <> b:
        total+=i

print 'Total: %s' % total
    
