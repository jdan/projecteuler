import math
from fractions import Fraction

total = 0

def isgood(x):
    if x == 1:
        return False
    i = 2
    while True:
        if x == 2 or x == 5:
            return True
        if x % i == 0:
            if not (i == 2 or i == 5):
                return False
            else:
                x /= i
                i = 2
        else:
            i+=1
            
for i in range(5,10001):
    parts  = round(i / math.e)
    good = False
    ex = False
    f = ''
    index = 0
    if not isgood(parts):
        f = str(Fraction(int(parts),i))
        index = f.find('/')
        if isgood(int(f[0:index])):
            good = True
            
    if int(parts) ** 2 == i:
        good = True
        
    if (isgood(parts) or good or ex):
        total += (-1 * i)
    else:
        total += i

    #print str(i) + ": " + str(int(parts)) + ": " + \
          #str((i / parts)) + " -> " + str(isgood(parts) or good)
        
print "Total: %s" % total
