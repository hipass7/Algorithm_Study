a = int(input())
num = a
cnt = 0

while 1:
    x, y = a // 10, a % 10
    z = x + y
    a = y * 10 + (z % 10)
    cnt += 1
    if a == num:
        break

print(cnt)