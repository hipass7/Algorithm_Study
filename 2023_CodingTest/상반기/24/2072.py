a = list(map(int, input().split()))

sum = 0
for i in range(len(a)):
    if a[i] % 2 == 1:
        sum += a[i]

print("#"+str(T)+" "+str(sum))