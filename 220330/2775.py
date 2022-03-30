case = int(input())

def f(k, n):
    if k == -1 or n == 1:
        return 1
    else:
        return f(k- 1, n) + f(k, n - 1)

for i in range(case):
    k = int(input())
    n = int(input())

    print(f(k, n))
    

# -1c 1 1 1 1
# 0c 1 2 3 4
# 1c 1 3 6 10
# 2c 1 4 10 20
# 3c 1 5 15 35
