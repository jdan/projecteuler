from math import sqrt

def isPrime(n):                
    i = 0
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2,int(sqrt(n)) + 1): 
        if n % i == 0:
            return False
        else:
            pass
    return True

def psr(n):
    h = int(sqrt(n))
    while True:
        if n % h == 0:
            return h
        else:
            h -= 1

product = 2

for i in range(3,100):
    if isPrime(i):
        product *= i

print psr(product) #% (10 ** 16)
