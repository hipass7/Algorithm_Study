num = int(input())

people = list(map(int, input().split()))

a, b = map(int, input().split())

cnt = 0
for i in range(num):
    people[i] -= a
    cnt += 1
    while people[i] > 0:
        people[i] -= b
        cnt += 1

print(cnt)
