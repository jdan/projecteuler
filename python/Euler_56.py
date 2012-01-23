## Project Euler 56 Solution by Jordan Scales
## 12/06/09
## Considering natural numbers of the form, a**b,
##    where a, b  100, what is the maximum digital sum?

a = 0
b = 0
_max = 0

for a in range(1,100):          # 1 to 100, probably not necessary
    for b in range(1,100):
        num = a ** b            # a^b
        dsum = 0
        for c in str(num):      # add each digit
            dsum += int(c)
        if dsum > _max:         # if greater than max, then set new max
            _max = dsum

print _max                      # print new max
