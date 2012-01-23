from math import sqrt

def gcd(num1, num2):
    a = max(num1, num2)
    b = min(num1, num2)
    for i in range(1,b+1):
        if not a % i and not b % i:
            g = i
    return g

def lcm(a, b):
    return a * b / gcd(a, b)

def factors(n):
    f = []
    for i in range(1,int(sqrt(n)) + 1):
        if not n % i:
            f.append(i)
            f.append(n / i)
    k = list(set(f))
    k.sort()
    return k

n = 1260
_max = 1000

while n < 1261:
    sol = 0
    if len(factors(n)) < 1000:
        for i in factors(n):
            p = i + n
            h = lcm(p, n)
            if 1.0/p + 1.0/h == 1.0/n:
                sol += 1
                print '1/%s + 1/%s = 1/%s' % (p, h, n)
                if sol > _max:
                    break
        if sol > _max:
            print n
            break
    n += 1
