# Euler 119 Solution
# Jordan Scales (http://jordanscales.com)
# 20 Aug 2013

def digitSum(n):
    return sum(map(int, list(str(n))))

res = []
for i in range(2, 100):
    for e in range(2, 50):
        if digitSum(i**e) == i:
            res.append(i**e)

res.sort()

print 'Result: %s' % res[29]
