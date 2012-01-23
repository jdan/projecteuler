def fib(n): #returns the nth number of the fibonacci sequence
    count = 0
    a = 1 #first number
    b = 1 #second number
    for count in range(2,n):
        a, b = a + b, a 
    return a

n = 1 #counter
fib_t = 1 #variable so fib() only has to launch once per trial
total = 0 #declare total (this will be the solution)

while fib_t < 4000000:
    if fib_t % 2 == 0: #filter out odd numbers
        total += fib_t
    else:
        pass
    n += 1
    fib_t = fib(n)

print total


        
