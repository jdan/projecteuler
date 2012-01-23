## Project Euler 17 Solution by Jordan Scales
## 12/05/09
## If all the numbers from 1 to 1000 (one thousand)
##   inclusive were written out in words, how many letters would be used?

import numparser

total = 0                              # total letters
alpha = 'abcdefghijklmnopqrstuvwxyz'   # check alphabet
count = 1                              # counter

for count in range(1,1000):
    string = numparser.parse(count)    # converts integer to 'string'
    chars = 0
    for char in string:                # checks to see if character is
        if char in alpha:              #   is in the alphabet
            chars+=1                  
    total += chars
    print '%s: %s: %s letters' % (count, string, chars) # diagnostics

total += len('onethousand')            # add 1000 (just a workaround for now)
print '1000: one thousand: %s letters' % len('onethousand')
print 'Total characters: %s' % total
