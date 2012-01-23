## Project Euler 52 Solution by Jordan Scales
## 12/06/09
## Find the smallest positive integer, x, such
##   that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

import math                            # we'll be using floor()
import sys                             # to exit

dec_places = 3                         # 6 combinations must be at least 3
                                       #    decimal places
def getchars(n):                       # function to rip characters from numbers
    s = str(n)
    c = ''
    chars = []
    for c in s:
        chars.append(c)
        
    chars.sort()
    return chars                       # return chars (in numerical order)

for dec_places in range(3,10):
    i = 0
    for i in range (10 ** (dec_places - 1), \
                    math.floor((10 ** (dec_places)) / 6)):  # all nums must be same length
        h = 0                                               #   6 * 13 = 98 (same length)
        for h in range(2,7):                                #   keep below 13%     
            if getchars(i) <> getchars(i * h):              # check if numbers are composed the same
                break
            else:
                if h == 6:                                  # if all 6 contain the same digits
                    print i                                 # print result
                    sys.exit(1)                             # kill program
                    
