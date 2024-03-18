num = int(input())

for i in range(num):
    x, y = map(str, input().split())
    x = int(x)
    li = []
    for j in range(len(y)):
        li.append(y[j] * x)
    for k in range(len(li)):
        print(li[k], end='')
    print()