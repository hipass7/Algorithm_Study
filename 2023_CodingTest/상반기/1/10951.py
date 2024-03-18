while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break

# 입력이 더 이상 들어오지 않거나 오류가 발생할 때, try-except를 사용하여 구현