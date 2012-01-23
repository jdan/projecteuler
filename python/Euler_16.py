## Project Euler 16 Solution by Jordan Scales
## 09/28/09
## What is the sum of the digits of the number 2^1000?

# Luckily, python can handle this giant number, so this is easy as pie

num = str(2 ** 1000)          # declare big number into string
i, t = 0, 0                   # some containers
for i in range(0, len(num)):  
    t += int(num[i])          # add each digit in the long number/string
 
print t                       # print result
