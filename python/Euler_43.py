import sys

inp = "0123456789"

letters = list(inp)
s = len(letters)
a = []
possible = []

total = 0

for c in range(s):
    a.append('')
    possible.append(0)    

def permutate(n):
    global total
    for i in range(s):
        if possible[i] == 0:
            possible[i] = 1
            a[n - 1] = letters[i]
            if n < s:
                permutate(n+1)
            else:
                # we've got a number
                if int(a[1] + a[2] + a[3]) % 2 == 0:
                    if int(a[2] + a[3] + a[4]) % 3 == 0:
                        if int(a[3] + a[4] + a[5]) % 5 == 0:
                            if int(a[4] + a[5] + a[6]) % 7 == 0:
                                if int(a[5] + a[6] + a[7]) % 11 == 0:
                                    if int(a[6] + a[7] + a[8]) % 13 == 0:
                                        if int(a[7] + a[8] + a[9]) % 17 == 0:
                                            found = int(''.join(a))
                                            total += found
                                            print found
                
            possible[i] = 0

permutate(1)

print 'Total: %s' % total
