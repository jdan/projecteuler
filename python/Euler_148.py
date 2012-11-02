#!/usr/bin/python

if __name__ == '__main__':
    limit = 10**9

    m = (7 * (7+1)) / 2
    t = m
    r = 7

    while r <= limit:
        t *= m
        r *= 7

    t /= m
    r /= 7

    total = 0
    row = 0
    index = 1
    mult = 1

    while t > 0:
        if limit - row >= r:
            total += t * index * mult
            index += 1
            row += r
        else:
            r /= 7
            t /= m
            mult *= index
            index = 1

    print 'Total: %s' % total

