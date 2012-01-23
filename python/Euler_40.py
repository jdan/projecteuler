## Project Euler 40 Solution by Jordan Scales
## 09/27/09

a = 0
s = ''
for a in range(0,1000000): # generate large string with all numbers
    s += str(a + 1)

print int(s[0]) * int(s[9]) * int(s[99]) * int(s[999]) \
      * int(s[9999]) * int(s[99999]) *  int(s[999999]) # multiply numbers
