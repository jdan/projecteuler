from itertools import permutations
from math import sqrt

def isPrime(n):
    if n == 2:
        return True
    if not n % 2:
        return False
    else:
        for i in range(3,int(sqrt(n)) + 1):
            if not n % i:
                return False
        return True
    
p = [1,2,3,4,5,6,7]
_max = 0

for k in list(permutations(p)):
    n = ''
    for j in k:
        n += str(j)
    if isPrime(int(n)):
        if n > _max:
            _max = n

print 'Found: %s' % _max
    
