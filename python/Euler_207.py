from math import sqrt, log

def Pinv(m):
    partitions = (int(sqrt(1 + 4*m)) - 1) / 2
    return float(partitions) / (int(log(partitions)) + 1)

p = 47964285056
print Pinv(47964285056)

