for a in range(100):
    for b in range(a, 101):
        try:
            if a % 10 <> 0 and b % 10 <> 0:
                l1 = list(str(a))
                l2 = list(str(b))

                for c in range(len(l1)):
                    if l1[c] in l2:
                        l2[l2.index(l1[c])] = ''
                        l1[c] = ''

                a2 = int(''.join(l1))
                b2 = int(''.join(l2))

                if a <> a2 and b <> b2:
                    if float(a) / float(b) == float(a2) / float(b2):
                        print '%s/%s -> %s/%s' % (a, b, a2, b2)
                
        except Exception:
            pass

            
                
