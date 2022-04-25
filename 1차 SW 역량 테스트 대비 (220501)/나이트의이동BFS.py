from collections import deque

t = int(input())

for tc in range(t):
    l = int(input())

    field = [[0] * l for _ in range(l)]
    x, y = map(int, input().split())
    fx, fy = map(int, input().split())

    def bfs(x, y):
        dx = [-2, -2, -1, -1, 1, 1, 2, 2]
        dy = [1, -1, 2, -2, 2, -2, 1, -1]

        queue = deque()
        queue.append((x, y))
        while queue:
            x1, y1 = queue.popleft()
            if x1 == fx and y1 == fy:
                return field[x1][y1]
            for i in range(8):
                nx = x1 + dx[i]
                ny = y1 + dy[i]

                if nx < 0 or nx > (l-1) or ny < 0 or ny > (l-1):
                    continue

                if field[nx][ny] == 0:
                    field[nx][ny] = field[x1][y1] + 1
                    queue.append((nx, ny))

    print(bfs(x, y))