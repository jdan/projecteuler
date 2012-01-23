from math import factorial

def digit_fact(n):
	return sum(map(factorial, map(int, list(str(n)))))
	
total = 0
	
for i in range(1, 1000000):
	l = [i]
	n = 1
	while True:
		a = digit_fact(l[-1])
	
		if a not in l:
			n += 1
			l.append(a)
		else:
			break
	if n == 60:
		total += 1

print 'Total: %s' % total
