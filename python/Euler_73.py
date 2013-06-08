# Euler 73
# by Jordan Scales (http://jordanscales.com)
# 8 Jun 2013
#
# How many fractions lie between 1/3 and 1/2 in the sorted
#   set of reduced proper fractions for d <= 12,000?

def frac_cmp(n1, d1, n2, d2):
    ''' Compares n1/d1 to n2/d2 '''
    # The trick is to avoid comparing to floats

    # First, multiply both sides by d1*d2
    #   Now, we have n1d2 <=> n2d1
    L = n1 * d2
    R = n2 * d1

    # Now, simply compare
    #   This only works for positive fractions
    if L == R:
        return 0
    elif L > R:
        return 1
    else:
        return -1

def gcd(a, b):
    ''' Greatest common divisor of a and b using 
        Euclid's algorithm '''
    while True:
        if a == 0:
            return b
        elif b == 0:
            return a
        if a == 1 or b == 1:
            return 1
        elif a > b:
            a -= b
        else:
            b -= a

def reduced(n, d):
    ''' Determines if n/d is reduced '''
    return gcd(n, d) == 1

if __name__ == '__main__':
    total = 0

    for d in range(4, 12001):
        lower_bound = d/3
        upper_bound = d/2

        for n in range(lower_bound, upper_bound+1):
            if reduced(n, d) and frac_cmp(n, d, 1, 3) == 1 and frac_cmp(n, d, 1, 2) == -1:
                total += 1

    print 'Total: %s' % total




