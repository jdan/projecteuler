# Euler 187 Solution
# Jordan Scales (http://jordanscales.com)
# 20 Aug 2013

m = 10**8
sieve = list(range(m/2))
sieve[1] = 0

i = 2
while i < m/4:
    if sieve[i] != 0:
        for d in range(i*2, m/2, i):
            sieve[d] = 0

    i += 1

print len(filter(lambda x: x != 0, sieve))
