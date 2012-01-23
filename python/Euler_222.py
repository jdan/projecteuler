from math import sqrt

total = 100

def pack(r1, r2):
    b = 100 - r1
    k = sqrt(2*r1*r2 + r1**2 - b**2 + 2*b*r2)
    return k + r2 - r1

for i in range(49,29,-1):
    total += pack(i + 1, i)


print 'Total: %s' % int(total * 1000)
