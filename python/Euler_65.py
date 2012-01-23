nums = [2, 3]
c = 2
i = 1

while len(nums) < 100:
	if c % 3 == 2:
		a = 2 * i * nums[-1] + nums[-2]
		i += 1
	else:
		a = nums[-1] + nums[-2]
		
	nums.append(a)
	c += 1
	
print 'Total: %s' % sum(map(int, list(str(nums[-1]))))
	

