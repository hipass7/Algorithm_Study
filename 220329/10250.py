num = int(input())

for i in range(num):
    h, w, n = map(int, input().split())
    floor = n % h
    if floor == 0:
        floor += 1
    room = (n - 1) // h + 1
    if n == h:
        room = 1
        floor = n
    
    if room // 10 == 0:
        print(floor, 0, room, sep='')
    else:
        print(floor, room, sep='')