num = int(input())
cnt = 0
for i in range(1, num + 1):
    i = str(i)
    if len(i) < 3:
        cnt += 1
    else:
        for j in range(len(i) - 1):
            n = int(i[j + 1]) - int(i[j])
            try:
                if int(i[j + 1]) + n == int(i[j+2]):
                    continue
                else:
                    break
            except:
                cnt += 1

print(cnt)

            