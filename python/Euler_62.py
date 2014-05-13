# Euler 62 Solution
# by Jordan Scales <scalesjordan@gmail.com>
# 12 May 2014

if __name__ == '__main__':
    N = 5
    digitHash = {}

    for i in range(1, 10**N):
        cube = i**3

        digits = list(str(cube))
        digits.sort()
        key = ''.join(digits)

        if key in digitHash:
            digitHash[key].append(i)
        else:
            digitHash[key] = [i]

    candidates = []
    for key in digitHash:
        items = digitHash[key]
        if len(items) == 5:
            candidates.append(items[0])

    print 'Answer: %d' % min(candidates)**3
