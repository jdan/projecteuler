## Project Euler 36 Solution by Jordan Scales
## 12/12/09
## What is the total of all the name scores in the file?

reader = file(r'C:\Python\Scripts\Project Euler\names.txt') # open file

total = 0

def evaluate(s,m):
    score = 0
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for char in s:
        score += alpha.find(char) + 1       # score each letter
    return score * m                        # mutiply total by location

names = []

whole = reader.read()
reader.close()

names = whole.split('","')    # split names into array
names[0] = names[0][1:]       # clean array ends
names[len(names) - 1] = names[len(names) - 1][:-1]
names.sort()   # sort names

for i in range(0,len(names)):  # score names
    score = evaluate(names[i], i+1)
    total += score

print 'Total: %s' % total   # print total
