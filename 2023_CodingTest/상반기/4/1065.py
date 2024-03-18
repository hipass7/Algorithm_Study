num = int(input())
cnt = 0
for i in range(1, num + 1):
    i = str(i)
    if len(i) < 3: # 두자리수의 경우
        cnt += 1
    else: # 세자리수의 경우
        for j in range(len(i) - 1):
            n = int(i[j + 1]) - int(i[j]) # 첫 자리와 두 번째 자리 비교 후 저장
            try:
                if int(i[j + 1]) + n == int(i[j + 2]): # 두 번째 자리와 세 번째 자리
                    continue
                else:
                    break
            except:
                cnt += 1

print(cnt)

            