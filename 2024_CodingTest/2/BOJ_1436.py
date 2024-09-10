n = int(input())
cnt = 0
ret = 666

while True:
    if "666" in str(ret):
        cnt += 1

    if cnt == n:
        break

    ret += 1

print(ret)