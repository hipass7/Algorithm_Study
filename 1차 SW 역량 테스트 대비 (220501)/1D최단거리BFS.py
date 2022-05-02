from collections import deque

n, k = map(int, input().split())

graph = [0] * 100001

queue = deque([n])

while True:
    n = queue.popleft()
    if n == k:
        print(graph[n])
        break
    for i in (n-1, n+1, 2 * n):
        if 0 <= i < 100001 and graph[i] == 0:
            queue.append(i)
            graph[i] = graph[n] + 1