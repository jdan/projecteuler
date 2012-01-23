## Project Euler 6 Solution by Jordan Scales
## 09/27/09
## Find the difference between the sum of the squares
##    of the first one hundred natural numbers and the square of the sum.

total1 = 0 
total2 = 0
i = 0 #counter

for i in range(1,101):
    total1 += i ** 2 # for set 1, add the squared number
    total2 += i      # for set 2, add the number, we'll square it later

total2 = total2 ** 2 # square the second set

print total2 - total1 #print the difference
