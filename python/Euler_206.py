# Euler 206 Solution
# Jordan Scales (http://jordanscales.com)
# 22 Aug 2013

from math import sqrt

_min = 10203040506070809
_max = 19293949596979899

for i in range(int(sqrt(_min)), int(sqrt(_max)) + 1):
    s = str(i**2)
    if s[0] == '1' and s[2] == '2' and s[4] == '3' and \
       s[6] == '4' and s[8] == '5' and s[10] == '6' and \
       s[12] == '7' and s[14] == '8' and s[16] == '9':
       print 'Result: %d' % i * 10
       break

