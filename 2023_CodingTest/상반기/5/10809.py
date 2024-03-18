num = input()
cnt = 97

li = [0] * 26
for i in range(26):
    for j in range(len(num)):
        if chr(cnt) == num[j]:
            li[i] = j
            break
        else:
            li[i] = -1
    cnt += 1

for i in range(len(li)):
    print(li[i], end=' ')