from math import sqrt

best_p = 0
max_s = 0

for p in range(7,1001):
    solutions = 0
    for a in range(1,p):
        for b in range(a,p):
            c = sqrt(a**2 + b**2)
            if int(c) == c:
                if a + b + c == p:
                    solutions += 1
    if solutions > max_s:
        max_s = solutions
        best_p = p

print 'Best perimeter: %s with %s soltuions' % (best_p, max_s)
