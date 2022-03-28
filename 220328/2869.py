import math
a, b, v = map(int, input().split())

# (A - B) * D + A >= V

d = math.ceil((v - a) / (a - b)) + 1

print(d)