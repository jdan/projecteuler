## Project Euler 10 Solution by Jordan Scales
## 09/27/09
## Find the sum of all the primes below two million.

# Using our isPrime() method from Problem #7
# NOTE: This takes forever to finish! I recommend using the C family or Java

def isPrime(n):                # function to check if n is prime
    i = 0
    for i in range(2,n/2 + 1): # to save CPU, we only count necessary numbers
        if n % i == 0:         # check if given number is divisible by anything
            return False
        else:
            pass
    return True

total = 0
n = 2

while n < 2000000:             # first 2 million numbers
    if isPrime(n):             # if prime, add it to the total
        total += n
    else:
        pass
    n += 1

print total                    # print result


