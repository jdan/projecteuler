import sys

def isPrime(n):
    if n == 2:
        return True
    if not n % 2:
        return False
    for i in range(3,int(n**0.5) + 1,2):
        if not n % i:
            return False
    return True

for a in range(1001,4000,2):
    if isPrime(a):
        for d in range(1000,5000):
            if isPrime(a+d) and isPrime(a + 2*d):
                t1 = str(a)
                t2 = str(a+d)
                t3 = str(a+d+d)
                s1 = list(t1)
                s2 = list(t2)
                s3 = list(t3)
                s1.sort()
                s2.sort()
                s3.sort()
                if s1 == s2 == s3:
                    if not t1 == '1487':
                        print 'Answer: %s' % (t1 + t2 + t3)
                        sys.exit(1)
