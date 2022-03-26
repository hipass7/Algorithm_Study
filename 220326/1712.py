a, b, c = map(int, input().split())

if b >= c:
    cnt = -1
else:
    i = a // (c - b) + 1
    cnt = i

print(cnt)