## Project Euler 48 Solution by Jordan Scales
## 09/29/09
## Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

# NOTE: Don't be intimidated by this one, Python has supports 'long'

total = 0                    # counters and such
i = 0

for i in range(1,1001):      # count from 1 to 1000, add i to its own power
    total += long(i ** i)

print str(total)[len(str(total))-11:len(str(total))-1]
                             # convert massive result to a string
                             # print the last 10 characters
