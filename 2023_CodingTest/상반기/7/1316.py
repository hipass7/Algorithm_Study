cnt = 0
num = int(input())
for i in range(num):
    li = []
    word = input()
    temp = True
    temp2 = ''

    for j in range(len(word)):
        if temp2 == word[j]:
            temp2 = word[j]
            continue
        else:
            temp2 = word[j]
            li.append(word[j])

    result = set(li)
    if len(result) == len(li):
        cnt += 1
        
print(cnt)

