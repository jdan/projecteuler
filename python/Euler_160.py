#!/usr/bin/python

def f(k):
    n = 1
    
    for i in range(2, k+1):
        n *= i
        while not (n % 10):
            n /= 10
        n %= 1000000
               
    return n % 100000
        
for k in range(1, 21):
    print '%d: %d' % (k, f(k*100000))