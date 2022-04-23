n = int(input())

for i in range(1, n+1):
    cnt = 0
    for j in range(len(str(i))):
        if str(i)[j] == '3' or str(i)[j] == '6' or str(i)[j] == '9':
            cnt += 1
    
    if cnt:
        print("-" * cnt, end=' ')
    else:
        print(i, end=' ')
