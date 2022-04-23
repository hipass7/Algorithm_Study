n = list(map(str, input()))

for i in range(1, len(n)):
    li1 = []
    li2 = []
    li1.append(n[:i])
    li2.append(n[i:2*i])
    if sorted(li1) == sorted(li2):
        cnt = i
        break

print(cnt)