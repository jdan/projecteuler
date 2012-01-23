entries = []

for a in range(2,101):
    for b in range(2,101):
        if a ** b in entries:
            pass
        else:
            entries.append(a**b)

print 'Total: %s' % len(entries)
