import sys

input = sys.stdin.readline

a, b = map(int, input().split())

m_list = [0] * 10001
cnt = 0
for i in range(b):
    m, p = map(int, input().split())
    m_list[p] += m

idx = 10000
while True:
    gram = m_list[idx]
    a -= gram
    cnt += gram * idx

    if a < 0:
        cnt += a * idx
        break

    idx -= 1

print(cnt)
