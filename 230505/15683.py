import copy

n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]
cctv = []

dx = [0, 1, 0, -1]  # 우, 하, 좌, 상
dy = [1, 0, -1, 0]


def dfs(cnt, arr):
    global result

    if cnt == len(cctv):
        num = 0
        for i in range(n):
            num += arr[i].count(0)
        result = min(result, num)
        return

    x, y, t = cctv[cnt]

    for k in direction[t]:
        temp = copy.deepcopy(arr)
        for i in range(len(k)):
            if k[i] == 1:
                nx, ny = x, y
                while True:
                    nx, ny = nx + dx[i], ny + dy[i]
                    if 0 <= nx < n and 0 <= ny < m:
                        if temp[nx][ny] == 6:
                            break
                        elif temp[nx][ny] == 0:
                            temp[nx][ny] = '#'
                    else:
                        break
        dfs(cnt + 1, temp)


direction = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]

for i in range(n):
    for j in range(m):
        if 1 <= office[i][j] <= 5:
            cctv.append([i, j, office[i][j]])

result = n * m
dfs(0, office)
print(result)