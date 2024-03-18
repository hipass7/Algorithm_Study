from collections import deque

def bfs(graph, start, visited, result):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        result.append(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

if __name__=="__main__":
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    visited = [False] * 9
    result = []

    bfs(graph, 1, visited, result)

    print(result)