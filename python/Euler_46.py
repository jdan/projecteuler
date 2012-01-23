def isPrime(n):
    if n == 2:
        return True
    if not n % 2:
        return False
    for i in range(3,int(n**0.5) + 1,2):
        if not n % i:
            return False
    return True

i = 33
going = True

while going:
    if not isPrime(i):
        k = 1
        while (k+1)**2 < (i / 2):
            k += 1
        while True:
            d = i - 2 * (k ** 2)
            if isPrime(d):
                i += 2
                break
            else:
                k -= 1
                if k == 0:
                    going = False
                    break
        ## print '%s = %s + 2 x %s ** 2' % (i, d, k)
    else:
        i += 2

print 'Answer: %s' % i
                    
