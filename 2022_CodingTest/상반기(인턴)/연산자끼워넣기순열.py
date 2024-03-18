import itertools

def perm(arr, n):
    result = []
    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])

    elif n > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            ans.remove(arr[i])
            for p in perm(ans, n-1):
                if ([arr[i]] + p) not in result:
                    result.append([arr[i]] + p)

    return result

n = int(input())
a = list(map(int, input().split()))
temp = list(map(int, input().split()))
op = []
# op = [0, 2]
for i in range(len(temp)):
    x = temp[i]
    for j in range(x):
        op.append(i)

# result = perm(op, len(op))
result = list(itertools.permutations(op, len(op)))
result = list(set(result))

cnt_list = []
sign = True
for i in range(len(result)):
    cnt = a[0]
    for _ in range(n - 1):

        if result[i][_] == 0:
            cnt += a[_+1]
        if result[i][_] == 1:
            cnt -= a[_+1]
        if result[i][_] == 2:
            cnt *= a[_+1]
        if result[i][_] == 3:
            if cnt < 0:
                cnt = -cnt
                sign = False
            cnt //= a[_+1]
            if not sign:
                cnt = -cnt
                sign = True

    cnt_list.append(cnt)

print(max(cnt_list))
print(min(cnt_list))