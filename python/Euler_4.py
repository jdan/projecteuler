## Project Euler 4 Solution by Jordan Scales
## 09/26/09
## Find the largest palindrome made from the product of two 3-digit numbers.

a = 1 # let's declare some variables
b = 1
c = 1

def isPalindrone(n):
    return str(n) == str(n)[::-1] # string is the same backwards and forwards

for a in range(1,1000):
    for b in range(1,1000):
        if isPalindrone(a * b) and a * b > c: 
            c = a * b # if product is palindrone, save it (if it's bigger)
        else:
            pass

print c
