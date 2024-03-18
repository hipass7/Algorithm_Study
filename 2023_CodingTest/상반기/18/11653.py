num = int(input())

li = []

cnt = 2

if num != 1:
    while True:
        if num % cnt == 0:
            num /= cnt
            li.append(cnt)
            cnt = 2
            continue
        if num == 1:
            break
        cnt += 1

for i in range(len(li)):
    print(li[i])
