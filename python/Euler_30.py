## Project Euler 30 Solution by Jordan Scales
## 10/3/09
## Find the sum of all the numbers that can be written
##    as the sum of fifth powers of their digits.

i = 0
added = 0
total = 0
for i in range(2,1000000):              # count to a reasonable number
    added = 0
    for c in range(0,len(str(i))):      # scroll through the string
        added += int(str(i)[c]) ** 5    # add digits (^5)
    if added == i:                      # is sum of digits (^5) == original?
        print i
        total += i                      # add to total

print 'Total: %s' % total               # print total
