def isBouncy(n):
    nums = []
    rnums= []
    for char in str(n):
        nums.append(char)
        rnums.append(char)
    nums.sort()
    rnums.sort()
    rnums.reverse()
    if str(n) == ''.join(nums) or str(n) == ''.join(rnums):
        return False
    else:
        return True

i = 1
b = 0
ratio = 0
stop = 21780
while True:
    if isBouncy(i):
        b += 1
    ratio = float(b) / i * 100
    if ratio == 99:
        print '%s percent @ %s' % (ratio, i)
        break
    i += 1
    if ratio > 99:
        print 'Something went wrong!'
        print ratio, i
        break
