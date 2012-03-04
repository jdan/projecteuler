#!/usr/bin/python

from math import sqrt

# R x 1 grid
#   R   1x1 squares
#   R-1 2x1 squares
#   R-2 3x1 squares
#   ...
#   1   Rx1 square
#   
#   R(R+1)/2 squares in 1 column
#   
#   For each added column, C(C+1)/2 choices added
#   
# For an RxC box, RC(R+1)(C+1)/4 choices

# RC(R+1)(C+1)/4 - 2,000,000 is a minimum
# R <- [2..sqrt(2,000,000)]
#   C(C+1) = 8,000,000/(R*(R+1))
#   C = sqrt(8,000,000/(R*(R+1)))

def rects(r, c):
  return r*c*(r+1)*(c+1) / 4

if __name__ == '__main__':
  R = 2
  C = 2
  min_c, min_r = C, R
  min_diff = abs(2000000 - rects(R,C))
  min_area = R*C
  
  for R in range(2, int(sqrt(2000000))):
    C = int(sqrt(8000000/(R*(R+1))))
    amt = rects(R, C)
    if abs(2000000 - amt) < min_diff:
      min_diff = abs(2000000 - amt)
      min_area = R*C
      min_c = C
      min_r = R
        
  print 'Min: (%s x %s) = %s (%s rects off), Area: %s' % (min_r, min_c, rects(min_r, min_c), min_diff, min_area)

