a = input()

a = a.upper()

li = {}

for i in range(len(a)):
    if a[i] in li:
        li[a[i]] += 1
    else:
        li[a[i]] = 1

max = 0
for key, val in li.items():
    if val > max:
        max = val
        key2 = key
    elif val == max:
        key2 = '?'

print(key2)