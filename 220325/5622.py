a = input()

li = []
cnt = 0
for i in range(len(a)):
    if ord(a[i]) >= 89: # 숫자에 알파벳이 4개 들어가는 것에 대한 예외처리를 해주어야함, S와 Y와 Z
        b = ord(a[i]) - 67
    elif ord(a[i]) >= 83:
        b = ord(a[i]) - 66
    else:
        b = ord(a[i]) - 65
    li.append(b)

for i in range(len(li)):
    li[i] = li[i] // 3
    cnt += (li[i] + 3)

print(cnt)
# A는 65