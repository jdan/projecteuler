# Euler 86 solution
# Jordan Scales (http://jordanscales.com)
# 19 Aug, 2013

from math import sqrt

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

# Determines whether a given number is a square
@memoize
def isSquare(n):
    return int(sqrt(n)) == sqrt(n)

# The number of pairs (x,y,z) x <= y < z such that (x+y)^2 + z^2 == n^2
def pairs(n):
    total = 0
    for b in range(1, int(n / sqrt(2))):
        a = n**2 - b**2
        if isSquare(n**2 - b**2):
            #print (int(sqrt(a)), b, n)
            total += int(sqrt(a)) / 2

    return total

# Returns the number of unique, integer-sided cuboids (with max-edge length M)
# such that the shortest distance from one corner to another (around edges)
# is an integer
def cuboidSolutions(m):
    return sum(map(pairs, range(1, m+1)))

print cuboidSolutions(1000)
