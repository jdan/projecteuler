gold = 1.618033988749895

p = 100

while True:
    num = int((long(gold ** p) - (1 - gold) ** p) / (5 ** 0.5))
    last = []
    first = []
    for char in str(num)[-9:]:
        last.append(char)
    for char in str(num)[:9]:
        first.append(char)
    last.sort()
    first.sort()
    ideal = ['1','2','3','4','5','6','7','8','9']
    if (p) % 500 == 0:
        print p
    if first == ideal:
        print "Result: %s" % (p)
        break
    else:
        p += 1
