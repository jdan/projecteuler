## Project Euler 19 Solution by Jordan Scales
## 12/12/09
## How many Sundays fell on the first of the month during the twentieth century?

import datetime                           # makes everything so much easier

total = 0

for year in range(1901,2001):             # scroll through years
    for month in range(1,13):             # months
        h = datetime.date(year, month, 1) # create a new datetime object
        if h.weekday() == 6:              # is the 1st sunday?
            total += 1

print "Total: %s" % total                 # display total
