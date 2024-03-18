T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    from collections import deque

    n = int(input())
    x = list(map(int, input().split()))

    queue = x

    sum = 0

    while queue:
        temp = max(queue)
        idx = queue.index(temp)
        for i in range(idx + 1):
            e = queue.pop(0)
            sum += (temp - e)

    print("#{} {}".format(test_case, sum))