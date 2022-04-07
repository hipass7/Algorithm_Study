a = int(input())

cnt = cnt1 = cnt2 = 0
while a >= 5:
    a -= 5
    cnt1 += 1

while a != 0:
    if a >= 3:
        a -= 3
        cnt2 += 1
    else:
        a += 2
        cnt1 -= 1
        cnt2 += 1
        if cnt1 < 0:
            cnt = -1
            break

cnt = -1 if cnt == -1 else cnt1 + cnt2

print(cnt)