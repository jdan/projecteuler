## Project Euler 34 Solution by Jordan Scales
## 09/28/09
## Find the sum of all numbers which are equal to
##    the sum of the factorial of their digits.

import math

i, a, total = 0, 0, 0
for i in range(10,100000):                    # count through reasonable numbers
    add = 0
    for a in range(0, len(str(i))):           # split up integer
        add += math.factorial(int(str(i)[a])) # add factorials of each digit
    if add == i:
        total += i                            # add to total if valid

print total                                   # print result
