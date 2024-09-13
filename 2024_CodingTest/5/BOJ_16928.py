n, m = map(int, input().split())

ladder = []
snake = []

for _ in range(n):
    a, b = map(int, input().split())
    ladder.append([a, b])

for _ in range(m):
    a, b = map(int, input().split())
    snake.append([a, b])

cnt = 0

queue = [1]

while True:
    if 100 in queue:
        break

    temp = []
    for item in queue:
        if item > 100:
            continue
        
        for i in range(1, 7):
            temp.append(item + i)

        
    for _ in range(len(temp)):
        check = temp[_]

        for l in ladder:
            if l[0] == check:
                temp[_] = l[1]
            
        for s in snake:
            if check == s[0]:
                temp[_] = s[1]

    queue = list(set(temp))
    cnt += 1

print(cnt)
