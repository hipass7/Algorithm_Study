from collections import deque

n, k = map(int, input().split())

field = [0] * 100001

def bfs():
    queue = deque([])
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            print(field[x])
            break

        for i in (x-1, x+1, 2 * x):
            if 0 <= i <= 100000 and not field[i]:
                field[i] = field[x] + 1
                queue.append(i)

bfs()
