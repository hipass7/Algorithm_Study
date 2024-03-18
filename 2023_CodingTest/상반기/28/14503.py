n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]

cnt = 0
while True:
    if graph[r][c] == 0:
        graph[r][c] = -1
        cnt += 1
    elif graph[r-1][c] != 0 and graph[r+1][c] != 0 and graph[r][c-1] != 0 and graph[r][c+1] != 0:
        if d == 0:
            r += 1
        elif d == 1:
            c -= 1
        elif d == 2:
            r -= 1
        elif d == 3:
            c += 1
        if graph[r][c] == 1:
            break
    elif graph[r-1][c] == 0 or graph[r+1][c] == 0 or graph[r][c-1] == 0 or graph[r][c+1] == 0:
        d -= 1
        if d == -1:
            d = 3
        if d == 0:
            r -= 1
        elif d == 1:
            c += 1
        elif d == 2:
            r += 1
        elif d == 3:
            c -= 1
        if graph[r][c] != 0:
            if d == 0:
                r += 1
            elif d == 1:
                c -= 1
            elif d == 2:
                r -= 1
            elif d == 3:
                c += 1

print(cnt)


