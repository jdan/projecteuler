import sys

inp = "0123456789"

letters = list(inp)
s = len(letters)
a = []
possible = []

tot = 1

for c in range(s):
    a.append('')
    possible.append(0)    

def permutate(n):
    global tot
    for i in range(s):
        if possible[i] == 0:
            possible[i] = 1
            a[n - 1] = letters[i]
            if n < s:
                permutate(n+1)
            else:
                # we've got a number
                d1 = int(a[0])
                d2 = int(a[1])
                d3 = int(a[2])
                d4 = int(a[3])
                d5 = int(a[4])
                d6 = int(a[5])
                d7 = int(a[6])
                d8 = int(a[7])
                d9 = int(a[8])
                d10 = int(a[9])
                
            possible[i] = 0

permutate(1)
