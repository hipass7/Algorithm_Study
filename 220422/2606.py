n = int(input())
k = int(input())

graph = [[0] * n for _ in range(n)]

for i in range(k):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = True
    graph[b - 1][a - 1] = True

queue = [0]
visited = [0]
result = []

while queue:
    start = queue.pop(0)
    for i in range(n):
        if graph[start][i]:
            if i not in visited:
                queue.append(i)
                visited.append(i)

print(len(visited) - 1)