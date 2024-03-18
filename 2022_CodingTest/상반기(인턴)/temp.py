from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n)]
v = v - 1
for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

for _ in range(n):
    graph[_].sort()

def bfs(v):
    visited = [0] * n
    result = []
    queue = deque()
    queue.append(v)
    result.append(v)
    visited[v] = True
    while queue:
        pt = queue.popleft()
        for i in graph[pt]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                result.append(i)
    return result

visited = [0] * n
result = []

def dfs(v):
    visited[v] = True
    result.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


dfs(v)
for i in range(len(result)):
     result[i] += 1
print(*result, sep=' ')
result = bfs(v)
for i in range(len(result)):
     result[i] += 1
print(*result, sep=' ')

