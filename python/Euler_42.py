alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
total = 0

tris = [1]
for n in range(2,200):
    tris.append(int(0.5 * n * (n + 1)))

f = file('words.txt','r')
text = f.read()
words = text.split('","')

words[0] = words[0][1:]
words[len(words) - 1] = words[len(words) - 1][:-1]

for word in words:
    val = 0
    for char in word:
        val += alpha.find(char) + 1
    if val in tris:
        total += 1
        print '%s: %s' % (word, val)

print 'Total: %s' % total


