# Euler 188 Solution
# Jordan Scales (http://jordanscales.com)
# 21 Aug 2013

def last8Digits(n):
    return n % 10**8

def tetration(n, k, acc):
    if k == 0:
        return acc
    else:
        print k, acc
        return tetration(n, k-1, last8Digits(n ** acc))

if __name__ == '__main__':
    print 'Result: %d' % tetration(1777, 1855, 1)
