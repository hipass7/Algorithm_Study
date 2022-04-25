n = int(input())

graph = [list(map(int, input())) for _ in range(n)]

def dfs(x, y):
    global cnt
    if x < 0 or x > (n-1) or y < 0 or y > (n-1):
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        cnt += 1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

result = []

for i in range(n):
    for j in range(n):
        cnt = 0
        if dfs(i, j) != False:
            result.append(cnt)

result = sorted(result)
print(len(result))
for _ in result:
    print(_)