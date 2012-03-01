#!/usr/bin/python
import urllib
from math import log

    # The approach
    # We are given a^b >? x^y
    #   a^b / x^y > 1
    #   How can we transform x into a?
    #
    # 3^5 = 4^x
    # x = log 3^5 / log 4
    # x = 5 log 3 / log 4

    # comp accepts p1, p2
    #   where each argument [x, y] represents x^y

def comp(p1, p2):
    # we want to turn p2[0] into p1[0], and modify p2[1]
    a = p2[1] * log(p2[0]) / log(p1[0])
    
    if p1[1] > a:
        return True
    else:
        return False
        
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
