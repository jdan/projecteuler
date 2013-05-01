# Project Euler 76 Solution by Jordan Scales
# 5/1/13
# How many different ways can one hundred be written
#   as a sum of at least two positive integers?

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
    print arrangements(100)
