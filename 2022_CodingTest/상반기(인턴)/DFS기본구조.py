def dfs(graph, v, visited, result):
    visited[v] = True
    result.append(v)

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited, result)

if __name__=="__main__":
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]

    visited = [False] * 9
    result = []

    dfs(graph, 1, visited, result)

    print(result)