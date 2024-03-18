from collections import deque

n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# BFS
visited = [False] * (n + 1)
result = []
queue = deque()
queue.append(v)
result.append(v)
visited[v] = True
while queue:
    pt = queue.popleft()
    for i in range(1, n+ 1):
        if graph[pt][i] == 1 and not visited[i]:
            visited[i] = True
            queue.append(i)
            result.append(i)

print(graph)
print(result)


