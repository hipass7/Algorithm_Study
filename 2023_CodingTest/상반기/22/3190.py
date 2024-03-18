n = int(input())
k = int(input())

field = [[0] * n for _ in range(n)]

for i in range(k):
    x, y = map(int, input().split())
    field[x - 1][y - 1] = -1

field[0][0] = 1

l = int(input())

location = []
for i in range(l):
    x, y = map(str, input().split())
    location.append((x, y))

x = y = d = 0

cnt = 0

head = [0, 0]
tail = [[0, 0]]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0] # 우 하 좌 상

while True:
    head[0] += dx[d]
    head[1] += dy[d]
    if head[0] < 0 or head[0] >= n or head[1] < 0 or head[1] >= n or field[head[0]][head[1]] == 1:
        break
    cnt += 1
    tail.append([head[0], head[1]])
    if field[head[0]][head[1]] == -1:
        field[head[0]][head[1]] = 1
    else:
        field[head[0]][head[1]] = 1
        field[tail[0][0]][tail[0][1]] = 0
        tail.pop(0)

    # 이동방향 바꾸는거 구현

    if len(location) != 0:
        if cnt == int(location[0][0]):
            if location[0][1] == 'L':
                d -= 1
            else:
                d += 1
            d %= 4
            location.pop(0)

print(cnt + 1)