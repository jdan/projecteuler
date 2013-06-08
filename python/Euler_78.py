# Project Euler 78 Solution by Jordan Scales
# 5/18/13
# Find the least value of n for which arrangements(n) + 1
#   is divisible by one million.

# memoize decorator
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
def sumways(n, lt):
    ''' returns the number of ways you can sum `n` using numbers no
        greater than `lt` '''
    if n == 0:
        # base case, return 1
        return 1
    else:
        # up until lt
        #   compute a new sumways using a smaller total and new lt
        #   making sure not to go into the negatives
        return sum([sumways(n - i, i) for i in range(1, lt + 1) if n - i >= 0])

def arrangements(n):
    ''' returns the number of ways you can sum `n` using 2 or
        more positive integers '''

    # equivalent to the ways you can sum n using numbers no
    #   greater than n-1
    return sumways(n, n-1)

if __name__ == '__main__':
    n = 300
    while 1:
        n += 1
        if (arrangements(n) + 1) % 1000000 == 0:
            break
        print n

    print n
