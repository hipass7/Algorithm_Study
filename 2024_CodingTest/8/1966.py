from collections import deque

tc = int(input())

for _ in range(tc):
    cnt = 0
    m, n = map(int, input().split())
    graph = list(map(int, input().split()))
    queue = deque(graph)
    
    while queue:
        cnt += 1
        max_item = 0
        for i in queue:
            if max_item < i:
                max_item = i
        
        while True:
            temp = queue.popleft()

            if temp == max_item:
                break
            else:
                queue.append(temp)
                n -= 1
                if n == -1:
                    n = len(queue) - 1

        if n == 0:
            print(cnt)
            break

        n -= 1
        if n == -1:
            n = len(queue) - 1



    

