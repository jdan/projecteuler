f = file('67_triangle.txt')
triangle = []

for line in f.readlines():
    l = line.split(' ')
    l[len(l)-1] = l[len(l)-1][:-1]
    triangle.append(l)

f.close()

h = 98
while h >= 0:
    for i in range(0,h+1):
        triangle[h][i] = int(triangle[h][i]) + max(int(triangle[h+1][i]),\
                                               int(triangle[h+1][i+1]))
    h -= 1

print "Max: " + str(triangle[0][0])

