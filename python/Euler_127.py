from math import sqrt

def gcd(a,b):
    _max = 0
    p,q = max(a,b), min(a,b)
    if not (p % q):
        return q
    for i in range(1, int(sqrt(q)) + 1):
        t = q / i
        if not (p % i) and not (q % i) and i > _max:
            _max = i
        if not (p % t) and not (q % t) and t > _max:
            _max = t
    return _max

def rad(n):
    p = 1
    d = 2
    factors = []
    while n > 1:
        if not n % d:
            if d not in factors:
                factors.append(d)
                p *= d
            n /= d
            d = 2
        else:
            d += 1
    return p

total = 0

for c in range(3,120000):
    for b in range(c/2,c):
        if gcd(c,b) == 1:
            a = c - b
            total += c * (a < b and rad(a*b*c) < c and gcd(a,c) and gcd(a,b))
    if not c % 1000:
        print c / 1000

print 'Total: %s' % total          
    
