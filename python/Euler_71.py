## Project Euler 71 Solution by Jordan Scales
## 12/12/09
## By listing the set of reduced proper fractions for
##   d <= 1,000,000 in ascending order of size, find
##   the numerator of the fraction immediately to the left of 3/7.

from fractions import Fraction           # fantastic module

d = 1.0
b_num = 0
b_denom = 0

for i in range(1, 1000000):              # could be more efficient
    num = round(i/7.0) * 3               # pick fractions close to 3/7
    denom = i
    while 3.0/7 - num/denom < 0:         # consider more fractions
        num -= 1
    if num % 3 == 0 and denom % 7 == 0:  # make sure the fraction isn't 3/7
        num -= 1
    else:
        diff = 3.0 / 7 - float(num) / denom # must be less than 3/7
        if diff < d:                     # smaller difference?
            d = diff
            b_num = num
            b_denom = denom

print Fraction(int(b_num),int(b_denom))  # only need the numberator, but it's
                                         #   interesting
