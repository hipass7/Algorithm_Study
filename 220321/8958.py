num = int(input())

cnt = 0
total = 0
for i in range(num):
    quiz = list(input())
    for j in range(len(quiz)):
        if quiz[j] == "O":
            cnt += 1
            total += cnt
        else:
            cnt = 0
    print(total)
    total = cnt = 0

        
