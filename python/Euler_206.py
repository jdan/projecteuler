start = 1000000000

while True:
    num = str(start**2)
    lis = [1,2,3,4,5,6,7,8,9,0]
    c = 0
    if len(num) > 19:
        print "Something went wrong!"
        break
    for i in range(0,19,2):
        if num[i] == lis[c]:
            break
        else:
            c+=1
    start+=10

print "Result: %s" % start
