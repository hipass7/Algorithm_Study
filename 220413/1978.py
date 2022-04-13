n = int(input())

num = list(map(int,input().split()))

cnt = len(num)
for i in num:
    div = 2
    if int(i) == 1:
        cnt -= 1
        continue
    while div < 1001:
        if int(i) % div == 0 and int(i) != div:
            cnt -= 1
            break
        div += 1
    
print(cnt)
