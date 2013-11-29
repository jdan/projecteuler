# Euler 188 Solution
# Jordan Scales (http://jordanscales.com)
# 21 Aug 2013

def last8Digits(n):
    return n % 10**8

# returns a^b
def exp_cut(a, b):
    if b == 0:
        return 1
    else:
        prod = last8Digits(exp_cut(a, b/2) * exp_cut(a, b/2))
        if b % 2 != 0: prod *= a

        return prod

# returns the last 8 digits of a^^b
def tetration_cut(a, b):



if __name__ == '__main__':
    #print 'Result: %d' % tetration(1777, 1855, 1)
    print exp_cut(1777, exp_cut(1777, 1777))
