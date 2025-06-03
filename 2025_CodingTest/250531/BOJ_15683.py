import copy

cctv = []
arr = []

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def check(xx, yy, dira):
    dira %= 4
    while True:
        nx = xx + dx[dira]
        ny = yy + dy[dira]
        xx, yy = nx, ny
        if nx < 0 or ny < 0 or nx >= N or ny >= M:
            return
        if arr[nx][ny] == 6:
            return
        if arr[nx][ny] != 0:
            continue
        arr[nx][ny] = -1

def dfs(idx):
    if idx == len(cctv):
        cnt = sum(row.count(0) for row in arr)
        return cnt

    x, y = cctv[idx]
    backup = [row[:] for row in arr]  # 깊은 복사

    min_val = float('inf')
    for dir in range(4):
        # 원상태로 복구
        for i in range(N):
            arr[i] = backup[i][:]

        if arr[x][y] == 1:
            check(x, y, dir)
        elif arr[x][y] == 2:
            check(x, y, dir)
            check(x, y, dir + 2)
        elif arr[x][y] == 3:
            check(x, y, dir)
            check(x, y, dir + 1)
        elif arr[x][y] == 4:
            check(x, y, dir)
            check(x, y, dir + 1)
            check(x, y, dir + 2)
        elif arr[x][y] == 5:
            check(x, y, dir)
            check(x, y, dir + 1)
            check(x, y, dir + 2)
            check(x, y, dir + 3)

        min_val = min(min_val, dfs(idx + 1))

    return min_val

# 입력
N, M = map(int, input().split())

for i in range(N):
    row = list(map(int, input().split()))
    arr.append(row)
    for j in range(M):
        if row[j] != 0 and row[j] != 6:
            cctv.append((i, j))

ret = dfs(0)
print(ret)
