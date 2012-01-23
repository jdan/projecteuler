def isPrime(n):
    if n == 2:
        return True
    if not n % 2:
        return False
    for i in range(3,int(n**0.5) + 1,2):
        if not n % i:
            return False
    return True

_max = 1000000
total = 0

for i in range(2,_max):
    circular = True
    s = str(i)
    if isPrime(i):
        for k in range(1,len(s)):
            s = s[1:] + s[0]
            if not isPrime(int(s)):
                circular = False
                break
    else:
        circular = False
    total += circular

print 'Total: %s' % total
