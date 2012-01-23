## Project Euler 9 Solution by Jordan Scales
## 09/27/09
## There exists exactly one Pythagorean triplet for which a + b + c = 1000.
## Find the product abc.
import math

a, b = 0, 0

for a in range(1,700):             # scroll through all viable numbers
    for b in range(1,700):
        c = math.sqrt(a**2 + b**2) # get c
        if a + b + c == 1000:      # check for sum to be 1000
            print a * b * c        # print result

# NOTE: This will spit out two answers (both the same) because we are
#       scrolling through both a and b
