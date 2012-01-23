## Project Euler 5 Solution by Jordan Scales
## 09/26/09
## What is the smallest number that is evenly divisible by all
##    of the numbers from 1 to 20?

## NOTE: This program may take several minutes to complete

def checkDiv(n):
    i = 0
    for i in range(1, 20): # count through 1 to 19 and check if i is divisible
        if n % i != 0:
            return False
        else:
            pass
    return True

i = 1
while not checkDiv(i): # count up until a number satisfies checkDiv()
    i += 1

print i
