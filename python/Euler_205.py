from fractions import Fraction

p_totals = [0] * 37
for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            for d in range(1, 5):
                for e in range(1, 5):
                    for f in range(1, 5):
                        for g in range(1, 5):
                            for h in range(1, 5):
                                for i in range(1, 5):
                                    p_totals[a + b + c + d + e + f + g + h + i] += 1

h_totals = [0] * 37
for a in range(1, 7):
    for b in range(1, 7):
        for c in range(1, 7):
            for d in range(1, 7):
                for e in range(1, 7):
                    for f in range(1, 7):
                        h_totals[a + b + c + d + e + f] += 1

prob = 0
p_totals = map(lambda i: Fraction(i, 4**9), p_totals)
h_totals = map(lambda i: Fraction(i, 6**6), h_totals)

for i in range(37):
    prob += h_totals[i] * sum(p_totals[i+1:])

print round(prob, 7)
