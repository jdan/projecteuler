## Project Euler 7 Solution by Jordan Scales
## 09/27/09
## What is the 10001st prime number?

def isPrime(n):                # function to check if n is prime
    i = 0
    for i in range(2,n/2 + 1): # to save CPU, we only count necessary numbers
        if n % i == 0:         # check if given number is divisible by anything
            return False
        else:
            pass
    return True

f = 0
n = 1
while f != 10001:
    n += 1
    if isPrime(n): # if prime, add one to a counter
        f += 1
    else:
        pass       # if counter reaches 10001, stop and print the result

print n
