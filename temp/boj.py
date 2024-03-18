n = int(input())

sum1 = 4
dot = 2

for i in range(1, n+1):
    s = 2 ** i

    sum1 = sum1 * 4 - (dot * 4) + 1

    dot = s + 1

print(sum1)
