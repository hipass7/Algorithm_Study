# 오목
from collections import deque

graph = [list(map(int, input().split())) for _ in range(19)]

dx = [0, 0, 1, 1, 1, -1, -1, -1]
dy = [1, -1, -1, 0, 1, -1, 0, 1]

result = 0
res = 0

for j in range(19):
    for i in range(19):  
        if graph[i][j] == 0:
            continue

        else:
            for k in range(8):
                queue = deque([(i,j)])
                cnt = 0
                while queue:
                    x, y = queue.popleft()
                    nx = x + dx[k]
                    ny = y + dy[k]

                    if nx < 0 or ny < 0 or nx > 18 or ny > 18:
                        continue

                    if graph[nx][ny] == 0:
                        continue

                    if graph[nx][ny] == graph[x][y]:
                        #graph[x][y] = 0
                        queue.append((nx, ny))
                        cnt += 1
                        result = graph[nx][ny]

                    if cnt == 4:
                        check_x = nx - 5 * dx[k]
                        check_y = ny - 5 * dy[k]
                        if check_x < 0 or check_y < 0 or check_x > 18 or check_y > 18:
                            res = result
                            continue

                        if graph[check_x][check_y] != graph[x][y]:
                            res = result
                            continue

                    if cnt > 4:
                        res = 0
                        continue

                if res > 0:
                    break

        if res > 0:
            break

        result = 0

    if res > 0:
        break

print(res)
if res > 0:
    print(i+1, j+1)
       