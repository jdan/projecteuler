## Project Euler 55 Solution by Jordan Scales
## 12/06/09
## How many Lychrel numbers are there below ten-thousand?

def isPalindrone(n):
    s = str(n)                # convert to string
    
    return s == s[::-1]:      # is it the same backwards and forwards?            

i = 0
total = 0
for i in range(1,10001):
    c = 0
    w = i
    isLychrel = True
    while c < 51:                         # check if 50 iterations have passed
        s = w + int(str(w)[::-1])         # add reverse
        if isPalindrone(s):               # check palindrone
            isLychrel = False
            break
        else:
            w = s                         # new number to reverse
            c += 1
    if isLychrel:
        total += 1                        # add one to total

print total                               # print total
