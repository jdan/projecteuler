def isPrime(n):
    if n == 1:
        return False
    prime = True
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            prime = False
    return prime

c = 0
n = 13
total = 0

while c < 11:
    n += 1
    prime = 1
    for k in range(0, len(str(n))):
        if not isPrime(n):
            prime *= 0
        if not isPrime(int(str(n)[-1*k:])):
            prime *= 0
        if not isPrime(int(str(n)[0:k+1])):
            prime *= 0
    if prime == 1:
        c+=1
        total += n
        print n
        
print 'Total: %s' % total
