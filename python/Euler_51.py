# Euler 51 Solution
# by Jordan Scales <scalesjordan@gmail.com>
# 12 May 2014

from math import sqrt

def eratosthenes(maxN):
    # An array full of True's to start
    primeMap = [True] * (maxN + 1)

    # 0 and 1 are not prime
    primeMap[0] = False
    primeMap[1] = False

    for i in range(2, int(sqrt(maxN)) + 1):
        if not primeMap[i]: continue

        a = 2*i
        while a < maxN + 1:
            primeMap[a] = False
            a += i

    return primeMap

# Returns a list of variations given a pattern
# Wildcards are set as '*'
#
# Example: variations('*3')
# => [13, 23, 33, 43, 53, 63, 73, 83, 93]
def variations(pattern):
    result = []

    # Edge case: patterns beginning with '*' should not have a
    # leading zero
    if pattern[0] == '*':
        startIndex = 1
    else:
        startIndex = 0

    for digit in range(startIndex, 10):
        result.append(int(pattern.replace('*', str(digit))))

    return result

# Generates all patterns of a given digit length
#
# Example: list(patterns(2))
# => ['1*', '2*', '3*', '4*', '5*', '6*', '7*', '8*', '9*',
#     '*1', '*2', '*3', '*4', '*5', '*6', '*7', '*8', '*9',
#     '**']
def patterns(length):
    def helper(leading, length, hasWildcard):
        # Edge case to make sure we don't have any leading zeros
        if leading:
            startIndex = 1
        else:
            startIndex = 0

        # First, yield a wildcard
        # Then, if we have a wildcard already, yield all the digits
        #
        # If we haven't had a wildcard yet, don't yield the digits, because
        # the pattern will consist of nothing but digits!
        if length == 1:
            yield '*'
            if hasWildcard:
                for digit in range(startIndex, 10):
                    yield str(digit)

        # Generate subpatterns and append to them a digit
        # Then, finally, a wildcard
        else:
            for subPattern in helper(False, length - 1, hasWildcard):
                for digit in range(startIndex, 10):
                    yield str(digit) + subPattern

            for subPattern in helper(False, length - 1, True):
                yield '*' + subPattern

    return helper(True, length, False)

if __name__ == '__main__':
    N = 6

    sieve = eratosthenes(10**N - 1)
    patternGenerator = patterns(N)

    biggestFamily = 0
    biggestFamilyPattern = ''
    biggestFamilySmallestMember = 0

    for pattern in patternGenerator:
        numbers = variations(pattern)
        minNumber = min(numbers)

        primes = filter(lambda i: sieve[i], numbers)
        if len(primes) > biggestFamily:
            biggestFamily = len(primes)
            biggestFamilySmallestMember = minNumber
            biggestFamilyPattern = pattern

    # print biggestFamilyPattern, biggestFamily, biggestFamilySmallestMember
    print 'Result: %d' % biggestFamilySmallestMember
