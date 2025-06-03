x = input()

length = len(x)
my_list = []
for _ in range(1, length):
    for i in range(length):
        if i+_ > length:
            break
        my_list.append(x[i:i+_])
my_list.append(x)

print(len(set(my_list)))
    
