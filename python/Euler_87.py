# Euler 87 Solution
# Jordan Scales (http://jordanscales.com)
# 20 Aug 2013

def memoize(f):
    if not hasattr(f, 'cache'):
        f.cache = {}

    def inner(*args):
        if f.cache.has_key(args):
            return f.cache[args]
        else:
            res = f.cache[args] = f(*args)
            return res

    return inner

@memoize
def isPrime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        i = 3
        while i**2 <= n:
            if n % i == 0:
                return False
            i += 2

        return True

# Returns a list of primes, which raised to the power e, are less than n
def expPrimesBelowN(n, e):
    i = 2
    res = []
    while i**e < n:
        if isPrime(i):
            res.append(i)
        i += 1
    return res

if __name__ == '__main__':
    m = 50000000
    squarePrimes = expPrimesBelowN(m, 2)
    cubicPrimes = expPrimesBelowN(m, 3)
    quarticPrimes = expPrimesBelowN(m, 4)

    print len({ a**2 + b**3 + c**4
                for a in squarePrimes
                for b in cubicPrimes
                for c in quarticPrimes
                if a**2 + b**3 + c**4 < m })

