#!/usr/bin/python
import urllib
from math import log

# LOGs are your best friend for this problem

def comp(p1, p2):
    # we want to turn p2[0] into p1[0], and modify p2[1]
    return p1[1] * log(p1[0]) > p2[1] * log(p2[0])
        
if __name__ == '__main__':
    reader = urllib.urlopen('http://projecteuler.net/project/base_exp.txt')
    pairs = [map(int, p.split(',')) for p in reader.readlines()]
    reader.close()
    
    line = 0
    best = pairs[0]
    
    for i, pair in enumerate(pairs[1:]):
        if comp(pair, best):
            best = pair
            line = i + 2   # enumerate is 0 at line 2
    
    print 'Best: %s, %s on line %s' % (best[0], best[1], line)
