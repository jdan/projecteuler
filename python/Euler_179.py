def factors(n):
    t = 0
    for i in range(1,int(n**(0.5))+1):
        if n % i == 0:
            t += 1
            if i**2 <> n:
                t += 1
    return t

total = 1
now = factors(2)
nxt = factors(3)

for i in range(3,10000000):
    now = nxt
    nxt = factors(i+1)
    if now == nxt:
        total += 1

print 'Total: %s' % total
