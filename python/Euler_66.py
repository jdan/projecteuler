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
        
def eval_frac(c_frac):
    c_frac = c_frac[::-1]
    num = c_frac[0]
    denom = 1
    
    for i in c_frac[1:]:
        num, denom = denom, num
        
        num += i * denom
        
    return num, denom
        
def pell_equation(d):
    c_frac = sqrt_cont_frac(d)
    loop = c_frac[1:]
    head = c_frac[0]
    i = 0
    
    build = [head]
    
    num = head
    denom = 1
    
    while 1:
        if num**2 - d * denom**2 == 1:
            return num, denom
        
        build.append(loop[i % len(loop)])
        i += 1
        
        num, denom = eval_frac(build)
            
if __name__ == '__main__':
    m = 0
    m_d = 0
    for d in range(2, 1001):
        if int(d**0.5) != d**0.5:
            p = pell_equation(d)
            if p[0] > m:
                m = p[0]
                m_d = d
                
    print 'Max: %s' % m_d