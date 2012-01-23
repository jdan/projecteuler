primes = []

def problem_58():
    side_length = 1
    ratio = 1
    total_diagonals = 1
    total_primes = 0
    
    while ratio > 0.1:
        side_length += 2
        total_diagonals += 4
        
        n = side_length
        
        br = n**2
        tr = (n-2)**2 + (n-1)
        tl = (n-2)**2 + 2*(n-1)
        bl = n**2 - (n-1)
        
        for val in [br, tr, tl, bl]:
            if val in primes or is_prime(val):
                total_primes += 1
                    
        ratio = float(total_primes) / total_diagonals

    print 'Length: %s' % side_length
            

def is_prime(n):
    if not (n % 2):
        return False
    else:
        for i in range(3, int(n**0.5)+1, 2):
            if not (n % i):
                return False
        primes.append(n)
        return True
    
if __name__ == '__main__':
    problem_58()