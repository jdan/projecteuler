## Project Euler 25 Solution by Jordan Scales
## 09/28/09
## What is the first term in the Fibonacci sequence to contain 1000 digits?

def fib(n):                  # returns the nth number of the fibonacci sequence
    count = 0
    a = 1                    # first number
    b = 1                    # second number
    for count in range(2,n):
        a, b = a + b, a 
    return a

i = 1
t = 1
while len(str(t)) < 1000:    # calculate until length is 1000
    t = fib(i)
    i += 1

print i - 1                  # will return the term AFTER the first with
                             #    1000 digits, so we subtract 1
