## Project Euler 53 Solution by Jordan Scales
## 12/06/09
## How many, not necessarily distinct, values of  nCr, for 1  n  100,
##    are greater than one-million?

def fact(n):                       # factorial function
    if n == 0:
        return 1                   # exception
    else:
        return n * fact(n-1)       # recursion <3

def nCr(n,r):                      # nCr function
    return fact(n) / (fact(r) * fact(n-r))

i = 0
r = 0
total = 0

for i in range(23,101):            # first one is at 23, info given to us
    for r in range(0, i + 1):      # r <= n in nCr
        if nCr(i, r) > 1000000:    # check if greater than 1000000
            total += 1             #  - add one to total

print total
