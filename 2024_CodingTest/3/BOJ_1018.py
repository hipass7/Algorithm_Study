n, m = map(int, input().split())

graph = []
ret = []

for _ in range(n):
    graph.append(input())

for i in range(n-7):
    for j in range(m-7):
        d1 = 0
        d2 = 0

        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y) % 2 == 0:
                    if graph[x][y] != 'B':
                        d1 += 1
                    if graph[x][y] != 'W':
                        d2 += 1
                else:
                    if graph[x][y] != 'W':
                        d1 += 1
                    if graph[x][y] != 'B':
                        d2 += 1

        ret.append(d1)
        ret.append(d2)

print(min(ret))