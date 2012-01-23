## Euler 102 by Jordan Scales
## Dec 20th, 2010

reader = file('triangles.txt')

total = 0

for line in reader.readlines():
    coords = map(int, line.split(','))
    # Points A B C
    x = coords[::2]
    y = coords[1::2]

    ## positive/negative intercepts
    y_pos = False
    y_neg = False

    x_pos = False
    x_neg = False

    ## AB
    if x[1] <> x[0]:
        m = (y[1] - y[0]) / float(x[1] - x[0])
        yi = -1 * m * x[0] + y[0]
    else: 
        yi = 0
    
    if m <> 0:
        xi = -1 * yi / m
    else:
        xi = 0

    if xi <= max(x[0], x[1]) and xi >= min(x[0], x[1]):
        if xi > 0:
            x_pos = True
        elif xi < 0:
            x_neg = True
        
    if yi <= max(y[0], y[1]) and yi >= min(y[0], y[1]):
        if yi > 0:
            y_pos = True
        elif yi < 0:
            y_neg = True

    ## BC
    if x[2] <> x[1]:
        m = (y[2] - y[1]) / float(x[2] - x[1])
        yi = -1 * m * x[1] + y[1]
    else:
        yi = 0

    if m <> 0:
        xi = -1 * yi / m
    else:
        xi = 0

    if xi <= max(x[1], x[2]) and xi >= min(x[1], x[2]):
        if xi > 0:
            x_pos = True
        elif xi < 0:
            x_neg = True

    if yi <= max(y[1], y[2]) and yi >= min(y[1], y[2]):
        if yi > 0:
            y_pos = True
        elif yi < 0:
            y_neg = True

    ## AC
    if x[2] <> x[0]:
        m = (y[2] - y[0]) / float(x[2] - x[0])
        yi = -1 * m * x[0] + y[0]
    else:
        yi = 0

    if m <> 0:
        xi = -1 * yi / m
    else:
        xi = 0

    if xi <= max(x[0], x[2]) and xi >= min(x[0], x[2]):
        if xi > 0:
            x_pos = True
        elif xi < 0:
            x_neg = True

    if yi <= max(y[0], y[2]) and yi >= min(y[0], y[2]):
        if yi > 0:
            y_pos = True
        elif yi < 0:
            y_neg = True

    
    ## check that they're all there
    if x_pos and x_neg and y_pos and y_neg:
        total += 1

reader.close()

print 'Total: %s' % total
    
