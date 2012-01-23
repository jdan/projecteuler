## Project Euler 20 Solution by Jordan Scales
## 09/28/09
## Find the sum of the digits in the number 100!

import math                          # factorial method can be found here

num = math.factorial(100)
i, c = 0, 0
for i in range(0,len(str(num)) - 1): # scroll through 100!
    c += int(str(num)[i])            # add individual digits

print c
