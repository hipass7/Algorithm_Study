cnt = 0
num = int(input())
for i in range(num):
    li = []
    word = input()
    temp = True
    temp2 = ''
    for j in range(len(word)):
        li.append(word[j])
        if word[j] in li and temp2 != word[j]:
            for k in range(len(li)):
                if word[j] != li[k]:
                    temp = False
                    break
                else:
                    continue
        else:
            continue
        temp2 = word[j]
    if temp:
        cnt += 1

print(cnt)

