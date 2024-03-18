def dfs(x, y):
    if x < 0 or x > (n-1) or y < 0 or y > (m-1):
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

if __name__=='__main__':
    n, m = map(int, input().split())

    graph = [list(map(int, input())) for _ in range(n)]

    cnt = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                cnt += 1

    print(cnt)