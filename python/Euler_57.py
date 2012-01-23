## Project Euler 57 Solution by Jordan Scales
## 05/22/10
## In the first one-thousand expansions of the continued fraction 
##    of sqrt(2), how many fractions contain a numerator with 
##    more digits than denominator?

nums = [3, 7]                                       # bases
dens = [2, 5]

count = 0                                           # initialize a total var

while len(nums) < 1000:
	nums.append(2 * nums[-1] + nums[-2])            # numerators and denominators
	dens.append(2 * dens[-1] + dens[-2])            #    follow a pattern
	
	if len(str(nums[-1])) > len(str(dens[-1])):     # check digits (ugly)
		count += 1
	
print 'Total: %s' % count
	
	
