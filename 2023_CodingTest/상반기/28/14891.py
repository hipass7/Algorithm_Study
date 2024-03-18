a = list(map(int, input()))
b = list(map(int, input()))
c = list(map(int, input()))
d = list(map(int, input()))

class Tire:
    def __init__(self, li):
        self.stack = li
        self.left = 6
        self.right = 2
        self.top = 0
        self.turn = 0

    def counter_clockwise(self):
        self.left += 1
        self.right += 1
        self.top += 1
        if self.left == 8:
            self.left = 0
        elif self.right == 8:
            self.right = 0
        elif self.top == 8:
            self.top = 0
        
    def clockwise(self):
        self.left -= 1
        self.right -= 1
        self.top -= 1
        if self.left == -1:
            self.left = 7
        elif self.right == -1:
            self.right = 7
        elif self.top == -1:
            self.top = 7

first = Tire(a)
second = Tire(b)
third = Tire(c)
fourth = Tire(d)
my_list = [first, second, third, fourth]
k = int(input())

for _ in range(k):
    n, d = map(int, input().split())
    if n == 1:
        first.turn = d
        if first.stack[first.right] != second.stack[second.left]:
            second.turn = -d
            if second.stack[second.right] != third.stack[third.left]:
                third.turn = d
                if third.stack[third.right] != fourth.stack[fourth.left]:
                    fourth.turn = -d
    if n == 2:
        second.turn = d
        if first.stack[first.right] != second.stack[second.left]:
            first.turn = -d
        if second.stack[second.right] != third.stack[third.left]:
            third.turn = -d
            if third.stack[third.right] != fourth.stack[fourth.left]:
                fourth.turn = d
    if n == 3:
        third.turn = d
        if second.stack[second.right] != third.stack[third.left]:
            second.turn = -d
            if first.stack[first.right] != second.stack[second.left]:
                first.turn = d 
        if third.stack[third.right] != fourth.stack[fourth.left]:
            fourth.turn = -d
    if n == 4:
        fourth.turn = d
        if third.stack[third.right] != fourth.stack[fourth.left]:
            third.turn = -d
            if second.stack[second.right] != third.stack[third.left]:
                second.turn = d
                if first.stack[first.right] != second.stack[second.left]:
                    first.turn = -d

    for _ in my_list:
        if _.turn == 1:
            _.clockwise()
        elif _.turn == -1:
            _.counter_clockwise()
        _.turn = 0

cnt = 0
if first.stack[first.top] == 1:
    cnt += 1
if second.stack[second.top] == 1:
    cnt += 2
if third.stack[third.top] == 1:
    cnt += 4
if fourth.stack[fourth.top] == 1:
    cnt += 8

print(cnt)