## Project Euler 3 Solution by Jordan Scales
## 09/26/09
## What is the largest prime factor of the number 600851475143?

n = 2 # this will be the divisor
comp = 600851475143 # the number we'll be working with

while comp != n:
    if comp % n == 0: # comp is divisible by n?
        comp = comp / n # change comp
        n = 2
    else:
        n += 1

print n
