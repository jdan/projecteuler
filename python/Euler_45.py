from math import sqrt

def tri(n):
    return n * (n + 1) / 2

def ispent(n):
    p = (1 + sqrt(1 + 24 * n)) / 6.0
    return p == int(p)

def ishex(n):
    p = (1 + sqrt(1 + 8 * n)) / 4
    return p == int(p)

k = 286

while True:
    tr = tri(k)
    if ispent(tr) and ishex(tr):
        print k
        print tr
        break
    k += 1
