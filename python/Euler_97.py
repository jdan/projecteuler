## Project Euler 97 Solution by Jordan Scales
## 12/12/09
## Find the last 10 digits of 28433 * (2 ^ 7830457) + 1

base = 1

for count in range(1,8):              # get up to step 10
    base *= 2

for count in range(17,7830458,10):    # for less runtime, step 10
    base *= 1024
    base = int(str(base)[-10:])       # trim to last 10 chars

base *= 28433                         # fix-up
base += 1

print str(base)[-10:]                 # one last trim
