# https://en.wikipedia.org/wiki/Pentagonal_number
def generalizaed_pent(n):
    if n % 2 == 0:
        n //= -2
    else:
        n = (n + 1) // 2
        
    return (3 * n * n - n) // 2

memo = {}
# https://en.wikipedia.org/wiki/Partition_function_(number_theory)#Recurrence_relations
def p(n):
    if n <= 0: return 0
    if n <= 1: return 1
    if n in memo: return memo[n]

    i = 1
    res = 0
    while True:
        j = generalizaed_pent(i)
        if j >= n: break

        res += (1 if i % 4 == 1 or i % 4 == 2 else -1) * p(n - j)
        i += 1

    memo[n] = res
    return res

i = 1
res = None
while True:
    res = p(i)
    if res % 1000000 == 0:
        # Off by one error
        print(i-1, res)
        break
    i += 1

