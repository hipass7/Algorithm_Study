from collections import deque

m, n, h = map(int, input().split())

graph = [list(list(map(int, input().split())) for _ in range(n)) for _ in range(h)]

tomato = []

for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 1:
                tomato.append((k, i, j))

def bfs(tomato):
    dx = [-1, 1, 0, 0, 0 ,0]
    dy = [0, 0, -1, 1, 0, 0] # 좌 우 상 하
    dz = [0, 0, 0, 0, -1, 1]

    queue = deque([])
    for i in tomato:
        queue.append(i)

    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or nx > (n-1) or ny < 0 or ny > (m-1) or nz < 0 or nz > (h-1):
                continue

            if graph[nz][nx][ny] == -1:
                continue

            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] += (graph[z][x][y] + 1)
                queue.append((nz, nx, ny))

    return

bfs(tomato)

maximum = 0
temp = False

for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] > maximum:
                maximum = graph[k][i][j]
            if graph[k][i][j] == 0:
                temp = True
                break
        if temp:
            break
    if temp:
        break

if temp:
    print(-1)
else:
    print(maximum - 1)
