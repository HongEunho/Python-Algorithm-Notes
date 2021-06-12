import sys
import heapq

n = int(input())
q1 = [] # 음수를 넣을 큐
q2 = [] # 양수를 넣을 큐

for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    if a < 0:
        heapq.heappush(q1, -a) # 절대값이 작은게 앞에 와야 하므로
    elif a > 0:
        heapq.heappush(q2, a) # 양수이므로 그대로 최소힙으로 구현
    else:
        if not q1:
            if not q2:
                print(0)
            else:
                print(heapq.heappop(q2))
        elif not q2:
            print(-heapq.heappop(q1))

        else:
            tmp1 = -heapq.heappop(q1)
            tmp2 = heapq.heappop(q2)

            if abs(tmp1) > abs(tmp2):
                print(tmp2)
                heapq.heappush(q1, -tmp1)

            else:
                print(tmp1)
                heapq.heappush(q2, tmp2)
