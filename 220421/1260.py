from collections import deque

n, m, v = map(int, input().split())
v = v-1
field = [[None] * n for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    field[a-1][b-1] = 1
    field[b-1][a-1] = 1

stack = []
queue = [v]
result = [v]
res = []
rem = [v]
rem1 = [v]

while True:
    temp = []
    for i in range(n):
        if (field[v][i] == 1) and (i not in rem):
            temp.append(i)
        
    temp = sorted(temp, reverse=True)
    stack += temp
    if len(stack) == 0:
        break
    v = stack.pop()
    rem.append(v)
    if v not in result:
        result.append(v)

while len(queue) != 0:
    temp = queue.pop(0)
    for i in range(n):
        if (field[temp][i] == 1) and (i not in rem1):
            queue.append(i)
            rem1.append(i)
    res.append(temp)

for i in result:
    print(i+1, end=' ')
print()
for i in res:
    print(i+1, end=' ')
print()
