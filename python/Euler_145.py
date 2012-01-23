def reverse(n):
    return int(str(n)[::-1])

def hasodd(n):
    s = list(str(n))
    even = ['2','4','6','8','0']
    for i in s:
        if i in even:
            return False
    return True

_max = long(1e9)
total = 0

for i in xrange(1,_max):
    if not i % 100000:
        print i / 100000
    if i % 10:
        k = reverse(i)
        total += hasodd(i+k)

print total
