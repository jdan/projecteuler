# Euler 82 Solution
# by Jordan Scales (http://jordanscales.com)
# 29 Nov 2013
#
# Minimal path from the right to left side of a matrix

# matrix = []
# f = open('matrix.txt')
# for line in f.readlines():
#     matrix.append(map(lambda s: int(s), line.split(',')))

matrix = [[131, 673, 234, 103, 18],
          [201, 96, 342, 965, 150],
          [630, 803, 746, 422, 111],
          [537, 699, 497, 121, 956],
          [805, 732, 524, 37,  331]]

memo = {}
def minimum_path(r, c, from_dir):
    if (r, c) in memo:
        return memo[(r, c)]
    elif c == len(matrix[r]) - 1:
        res = matrix[r][c]
        memo[(r, c)] = res
        return res
    else:
        choices = []

        if from_dir != 'up' and r > 0:
            # check up
            choices.append(minimum_path(r - 1, c, 'down'))

        if from_dir != 'down' and r < len(matrix) - 1:
            # check down
            choices.append(minimum_path(r + 1, c, 'up'))

        # check right
        choices.append(minimum_path(r, c+1, 'left'))

        res = matrix[r][c] + min(choices)
        memo[(r, c)] = res
        return res

leftCol = [minimum_path(r, 0, '') for r in range(len(matrix))]
print leftCol
