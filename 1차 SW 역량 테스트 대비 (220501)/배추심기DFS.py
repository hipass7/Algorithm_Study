import sys
sys.setrecursionlimit(10**6)

t = int(input())

def dfs(x, y):
    global graph
    global m, n
    if x < 0 or x > (n-1) or y < 0 or y > (m-1):
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

for kk in range(t):
    m, n, k = map(int, input().split())

    graph = [[0] * m for _ in range(n)]

    for i in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    cnt = 0

    for i in range(n):
        for j in range(m):
            if dfs(i, j) != False:
                cnt += 1

    print(cnt)