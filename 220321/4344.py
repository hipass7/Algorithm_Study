num = int(input())

for i in range(num):
    li = list(map(int, input().split()))
    cnt = 0
    avg = sum(li[1:]) / li[0]
    for j in li[1:]:
        if j > avg:
            cnt += 1
    result = cnt / li[0] * 100
    print("%.3f" % (result) + "%")
