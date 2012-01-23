from math import sqrt

total = 0

for p in range(7,1500001):
    if not p % 1000:
        print p
    solutions = 0
    for a in range(1,p):
        for b in range(a,p):
            c = sqrt(a**2 + b**2)
            if int(c) == c:
                if a + b + c == p:
                    solutions += 1
    if solutions == 1:
        total += 1

print 'Total: %s' % total
