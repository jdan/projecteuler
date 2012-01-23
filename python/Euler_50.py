primes = [2, 3]
for i in range(5, 1000000, 2):
    if i % 1000 == 1:
        print i
        
    isp = True
    for p in primes:
        if p > i / 2 + 1:
            break
        if i % p == 0:
            isp = False
            break
            
    if isp:
        primes.append(i)
        
print 'Done!'
print len(primes)
            