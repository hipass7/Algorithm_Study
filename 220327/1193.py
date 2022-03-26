a = int(input())

i = 1
cnt = 0
while i // a == 0:
    cnt += 1
    i += (cnt + 1)

b = i % a

if cnt % 2 == 0:
    num = 1 + b
    div = cnt + 1 - b
else:
    div = 1 + b
    num = cnt + 1 - b    



print(num, "/", div, sep="")