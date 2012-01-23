goal = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

for n in range(10000):
    m = 1
    s = ''
    while len(s) < 9:
        s += str(n * m)
        m += 1

    k = list(s)
    k.sort()

    if k == goal:
        print s
        
    
