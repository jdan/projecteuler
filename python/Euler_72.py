#!/usr/bin/python

def euler72(limit):
    sieve = range(int(limit) + 1)
    for i in range(2, len(sieve)):
        if sieve[i] != i:
            continue
        for j in range(i, len(sieve), i):
            sieve[j] *= i - 1
            sieve[j] /= i
            
    return sum(sieve) - 1        
    
if __name__ == '__main__':
    print euler72(1e6)