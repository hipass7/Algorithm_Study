n1 = int(input())
n2 = int(input())
num = []

for i in range(n1, n2+1):
    div = 2
    if i == 1:
        continue
    while div < (i + 1):
        if i % div == 0 and i != div:
            break
        elif i == div:
            num.append(i)
        div += 1
    
if len(num) == 0:
    print(-1)
else:
    print(sum(num))
    print(num[0])
