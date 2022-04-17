num = int(input())

people = list(map(int, input().split()))

a, b = map(int, input().split())

cnt = 0
for i in range(num):
    people[i] -= a
    if people[i] < 0:
        cnt += 1
        continue
    else:
        div = people[i] // b
        th = people[i] % b
        cnt += (div + 1)
        while th > 0:
            th -= b
            cnt += 1

print(cnt)
