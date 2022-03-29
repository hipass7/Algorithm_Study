num = int(input())

for i in range(num):
    h, w, n = map(int, input().split())
    floor = n % h

    room = n // h + 1

    if n % h == 0:
        room = n // h
        floor = h
    
    if room // 10 == 0:
        print(floor, 0, room, sep='')
    else:
        print(floor, room, sep='')