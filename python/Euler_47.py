def f(n,m=1000):
    factors = []
    t = 0
    d = 2
    while n > 1:
        if not n % d:
            if d not in factors:
                factors.append(d)
                t += 1
            n /= d
            d = 2
        else:
            d += 1
        if t > m:
            return -1
    return t

i = [644,645,646,647]

while True:
    r = True
    for j in i:
        if f(j,4) <> 4:
            r = False
            break
    if r == True:
        print i[0]
        break
    else:
        i = i[1:] + [i[3] + 1]
