# 입력
#1 sys.stdin.readline() == input() 이지만, 코테에서는 보통 input()을 사용
import sys
a1 = int(sys.stdin.readline())

#2 1개의 정수 입력
a2 = int(input())

#3 정해진 개수의 정수를 한 줄에 입력받을 때 (띄어쓰기 구분)
a3, b3, c3 = map(int, input().split())

#4 임의의 개수의 정수를 한 줄에 입력받아 리스트에 저장할 때 (띄어쓰기 구분)
a4 = list(map(int, input().split()))

#5 임의의 개수의 정수가 한 줄에 있고 n줄로 이루어진 2차원 리스트 (그래프)
li5 = []
n5 = int(input())
for i in range(n5):
    li5.append(list(map(int, input().split())))

#6 문자열 n줄을 입력받아 리스트에 저장할 때
n6 = int(input())
li6 = [input().strip() for i in range(n6)]

# 출력
#7 리스트에 있는 문자열을 하나의 문자열로 변환 후 출력
li7 = ['a', 'b', 'c']
print("".join(li7))        # 'abc' 출력
print("_".join(li7))        # 'a_b_c' 출력

#8 리스트에 있는 문자열 혹은 정수를 띄어쓰기 간격을 두고 출력
li8 = [1, 2, 3]
print(*li8)



