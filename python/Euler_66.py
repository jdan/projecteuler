from math import sqrt

_max = 0
_maxD = 0

def expand(n):
    frac = []
    while True:
        a = int(n)
        frac.append(a)

        n -= a
        if n < 0.00001: break
        n = 1.0/n

        if n == int(n):
            frac.append(int(n))
            break
    return frac

def compress(frac):
    n = frac[-1]
    d = 1
    for i in range(2, len(frac)+1):
        # XOR swap
        n = n ^ d
        d = n ^ d
        n = n ^ d
        n += d * frac[-i]
    return [n, d]

for d in range(2, 1001):
    if sqrt(d) != int(sqrt(d)):
        f = expand(sqrt(d))
        a = 0
        b = 0
        for i in range(2, len(f)):
            q = compress(f[:i])
            a = q[0]
            b = q[1]
            if a**2 - d * (b**2) == 1:
                if a > _max:
                    _max = a
                    _maxD = d
                break
        print '%s^2 - %sx%s^2 = 1' % (a, d, b)

