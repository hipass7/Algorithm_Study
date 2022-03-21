    # x, y = map(int, input().split())
    # print("Case #%d: %d + %d =" %(i+1, x, y), x+y)
    # num_list = list(map(int, input().split()))

num = int(input())
num_list = list(map(int, input().split()))
m = max(num_list)

li = []
for i in num_list:
    li.append(i / m * 100)
avg = sum(li) / num
print(avg)

# num_list = list(map(int, input().split())) 이 표현에 적응할 것!