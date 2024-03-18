from collections import deque

t = int(input())

for tc in range(t):
    v, e = map(int, input().split())

    vertex = [0] * (v + 1)
    graph = [[] for _ in range(v + 1)]

    for i in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    queue = deque()
    group = 1
    result = True
    for i in range(1, v+1):
        if vertex[i] == 0:
            queue.append(i)
            vertex[i] = group
            while queue:
                a = queue.popleft()
                for temp in graph[a]:
                    if vertex[temp] == 0:
                        queue.append(temp)
                        vertex[temp] = -vertex[a]
                    elif vertex[temp] == vertex[a]:
                        result = False
                        break
                if not result:
                    break
        if not result:
            break

    if result:
        print("YES")
    else:
        print("NO")