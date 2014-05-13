# Euler 108 Solution
# Jordan Scales <scalesjordan@gmail.com>
# 10 Mar 2014

memo = {}
def gcd(a, b):
    if (a, b) in memo:
        return memo[(a, b)]
    elif b == 0:
        memo[(a, b)] = a
        return a
    else:
        result = gcd(b, a % b)
        memo[(a, b)] = result
        return result

def lcm(a, b):
    return (a * b) / gcd(a, b)

# Computes the number of distinct solutions for the equation
# 1/x + 1/y = 1/n
def distinctSolutions(n):
    # x = n+1 and x = 2n offer two solutions right off the bat
    #
    # Also, x = 2n is the greatest value of x we need to check before
    # we repeat
    solutions = 2

    for x in range(n+2, 2*n):
        yCandidate = lcm(n, x)

        if yCandidate != n * x:
            denom = (yCandidate / x) + 1
            if yCandidate % denom == 0 and yCandidate / denom == n:
                # print "1/%d + 1/%d = 1/%d" % (x, yCandidate, n)
                solutions += 1

    return solutions

i = 4
while distinctSolutions(i) <= 40:
    i += 1

print 'Result: %d' % i
