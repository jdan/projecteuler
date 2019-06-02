# Euler 82 Solution
# by Jordan Scales (http://jordanscales.com)
# 29 Nov 2013
# revised 1 Jun 2019
#
# Minimal path from the right to left side of a matrix

matrix = []
f = open('matrix.txt')
for line in f.readlines():
    matrix.append(map(lambda s: int(s), line.split(',')))

# matrix = [[131, 673, 234, 103, 18],
#           [201, 96, 342, 965, 150],
#           [630, 803, 746, 422, 111],
#           [537, 699, 497, 121, 956],
#           [805, 732, 524, 37,  331]]

def graph_of_matrix(matrix):
    graph = {
        'init': {},
        'end': {},
    }

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            graph[(r, c)] = {}

            if c == 0:
                graph['init'][(r, c)] = 0

            if r > 0:
                graph[(r, c)][(r - 1, c)] = matrix[r][c]

            if r < len(matrix) - 1:
                graph[(r, c)][(r + 1, c)] = matrix[r][c]

            if c == len(matrix[r]) - 1:
                graph[(r, c)]['end'] = matrix[r][c]
            else:
                graph[(r, c)][(r, c + 1)] = matrix[r][c]

    return graph

def dijkstra(graph, start, end):
    Q = set([])
    dist = {}

    for v, _ in graph.items():
        dist[v] = float('inf')
        Q.add(v)

    dist[start] = 0

    while len(Q) > 0:
        u = min(Q, key=lambda v: dist[v])
        Q.remove(u)

        if u == end:
            return dist[end]
        else:
            for neighbor, _ in graph[u].items():
                if neighbor in Q:
                    alt = dist[u] + graph[u][neighbor]
                    if alt < dist[neighbor]:
                        dist[neighbor] = alt


print dijkstra(graph_of_matrix(matrix), 'init', 'end')
