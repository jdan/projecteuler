from math import sqrt
MAX = 10000000

nums = list(range(MAX))
for i in range(2, MAX):
    if nums[i] == i:
        for j in range(i, MAX, i):
            nums[j] *= i - 1
            nums[j] /= i

min_n = None
min_ratio = None

for i in range(2, MAX):
    # palindrone?
    if sorted(str(i)) == sorted(str(nums[i])):
        ratio = float(i) / nums[i]
        if min_ratio is None or ratio < min_ratio:
            min_n = i
            min_ratio = ratio

print "min_n:", min_n
print "min_ratio:", min_ratio
