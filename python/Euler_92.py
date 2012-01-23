def chain(n):
    t = 0
    for i in str(n):
        t += int(i) ** 2
    return t

total = 0

for k in range(1,10000000):
    t = k
    if not k % 100000:
        print k
    while True:
        t = chain(t)
        if t == 1 or t == 89:
            break
    total += (t == 89)

print total
    
