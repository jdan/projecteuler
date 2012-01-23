from math import sqrt

t = 10 ** 12 + 1

def is_int(n):
	return n == int(n) and n > 0
	
f    = lambda n    : (2 + 2*sqrt(2*n**2 - 2*n - 1)) / 4
f_i  = lambda n    : (2 - 2*sqrt(2*n**2 - 2*n - 1)) / 4
odds = lambda a, b : (float(a) / b) * (float(a-1) / (b-1))

while True:
	while not is_int(f(t)) and not is_int(f_i(t)):
		t += 1
		
	if odds(f(t), t) == 0.5 or odds(f_i(t), t) == 0.5:
		print 'Total discs: %s' % t

		if is_int(f(t)):
			a = int(f(t))
		else:
			a = int(f_i(t))

		print 'Blue discs: %s' % a
		
		break
	else:
		t += 1
