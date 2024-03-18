
a = int(input())

i = 1
cnt = 0
while i // a == 0:
    cnt += 1
    i += cnt * 6

print(cnt + 1)