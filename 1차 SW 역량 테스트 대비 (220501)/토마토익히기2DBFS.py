from collections import deque

m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

tomato = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            tomato.append((i, j))

def bfs(tomato):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1] # 좌 우 상 하

    queue = deque([])
    for i in tomato:
        queue.append(i)

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > (n-1) or ny < 0 or ny > (m-1):
                continue

            if graph[nx][ny] == -1:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] += (graph[x][y] + 1)
                queue.append((nx, ny))

    return

bfs(tomato)

maximum = []
temp = False

for i in range(n):
    maximum.append(max(graph[i]))
    if 0 in graph[i]:
        temp = True

if temp:
    print(-1)
else:
    print(max(maximum) - 1)
