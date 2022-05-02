from collections import deque

n = int(input())
k = int(input())
graph = [[] for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

queue = deque([0])

visited = [0]
while queue:
    pt = queue.popleft()
    for i in graph[pt]:
        if i not in visited:
            visited.append(i)
            queue.append(i)

print(len(visited) - 1)