from math import sqrt

limit = 100000000

sieve = { 1: False }
for i in range(2, int(sqrt(limit)) + 1):
    if i not in sieve:
        for j in range(2 * i, limit + 1, i):
            sieve[j] = False

total = 0
for i in range(1, limit + 1):
    if i > 2 and i not in sieve:
        continue

    all_prime = True
    divisors = []
    for j in range(1, int(sqrt(i)) + 1):
        if i % j == 0:
            divisors.append(j)
            if j + i / j in sieve:
                all_prime = False
                break
    if all_prime:
        # print i
        total += i

print 'Total', total