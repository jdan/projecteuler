# Euler 104
# 2 Jun 2019

a = 1
b = 1
n = 2

def pandigital(n):
    d = set([])
    while n > 0:
        d.add(n % 10)
        n //= 10

    return d == set([1, 2, 3, 4, 5, 6, 7, 8, 9])

while True:
    if pandigital(b % 1000000000) and pandigital(int(str(b)[:9])):
        print n
        break

    a, b = b, a + b
    n += 1
