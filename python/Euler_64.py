#!/usr/bin/python

def sqrt_cont_frac(n):
    head = int(n**0.5)
    if head == n**0.5:
        return [head]
    
    num = head
    denom = n - head**2
    
    a = [head]
    states = []
    
    while 1:
        pull = (head + num) / denom
        num -= pull*denom
        
        for state in states:
            if state == [pull, num, denom]:
                return a
                
        states.append([pull, num, denom])
        a.append(pull)
        
        denom = (n - num**2) / denom
        num *= -1
    
def e64():
    have_odd_period = 0
    for j in range(2, 10001):
        period = len(sqrt_cont_frac(j)) - 1
        if period % 2:
            have_odd_period += 1
            
    print 'Total: %s' % have_odd_period
    
if __name__ == '__main__':
    e64()