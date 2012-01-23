def isPrime(n):                
    i = 0
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2,n/2 + 1): 
        if n % i == 0:
            return False
        else:
            pass
    return True

c_max = 0
best_a = 0
best_b = 0

for a in range(-999,1000):
    if isPrime(abs(a)):
        for b in range(abs(a),1000):
            if isPrime(abs(b)):
                c = 0
                p = c**2 + a * c + b
                while isPrime(p):
                    c += 1
                    p = c**2 + a * c + b
                if c > c_max:
                    c_max = c
                    best_a = a
                    best_b = b
            else:
                pass
    else:
        pass

print 'a: %s, b: %s, n^2 + %sn + %s -> %s primes' % \
      (best_a, best_b, best_a, best_b, c_max - 1)
print 'Product: %s' % (best_a * best_b)
