f = file('keylog.txt','r')
s = []

for line in f.readlines():
	c = 0
	for char in line:
		if char in map(str, range(1,10)):
			n = int(char)
			if not n in s:
				s.append(n)
			else:
				if c > 0:
					a = s.index(int(line[c]))
					b = s.index(int(line[c-1]))
					if b > a:
						for k in range(a, b):
							s[k] = s[k] ^ s[k+1]
							s[k+1] = s[k] ^ s[k+1]
							s[k] = s[k] ^ s[k+1]
		c += 1
			
f.close()
print ''.join(map(str, s)) + '0'
