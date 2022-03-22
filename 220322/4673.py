num = set(range(10000))
a = set()

for i in range(10000):
    for j in str(i):
        i += int(j)

    a.add(i)

result = sorted(num - a)
for i in result:
    print(i)