## Project Euler 36 Solution by Jordan Scales
## 12/12/09
## Find the sum of all numbers, less than one million,
##    which are palindromic in base 10 and base 2.

total = 0

def isPalindrone(n):              
    return str(n) == str(n)[::-1]  # same backwards and forwards

def toBinary(n):
    c = 0
    b = 0
    while n > 0:
        c = 0
        while n >= 2**c: c += 1    # find which place to start in 
        c -= 1                     # fix
        b += 10 ** c               # add to binary
        n -= 2 ** c                # subtract
    return b

for i in range(1,1000000):
    if isPalindrone(i):            # no need to check binary unless
        b = toBinary(i)            #    this one works
        if isPalindrone(b):
            total += i             # add to total

print "Total: %s" % total          # print result
