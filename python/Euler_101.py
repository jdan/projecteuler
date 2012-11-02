#!/usr/bin/python

def BOP(ls):
    if len(ls) == 1:
        return ls[0]
    else:
        # compute the deltas
        deltas = []
        old = ls[0]
        for new in ls[1:]:
            deltas.append(new - old)
            old = new
        # BOP(seq) = seq[-1] + BOP(delta(seq))
        return ls[-1] + BOP(deltas)

if __name__ == '__main__':
    # get the first 10 terms
    f = lambda n: 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10
    terms = map(f, xrange(1, 11))

    total = 0
    for k in xrange(1, 11):
        total += BOP(terms[:k])

    print 'Total: %s' % total