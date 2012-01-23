_sum = 0

for a in range(1,10):
    for b in range(0,100):
        _sum += b == len(str(a**b))

print _sum
