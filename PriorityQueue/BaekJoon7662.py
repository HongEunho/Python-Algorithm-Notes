import heapq

t = int(input())

for i in range(t):
    k = int(input())
    q1, q2 = [], []
    visited = [False] * k

    for j in range(k):
        com, num = input().split()

        if com == 'I':
            heapq.heappush(q1, (int(num), j))
            heapq.heappush(q2, (-int(num), j))
            visited[j] = True

        else:
            if num == '1':
                while q2 and not visited[q2[0][1]]:
                    heapq.heappop(q2)
                if q2:
                    visited[q2[0][1]] = False
                    heapq.heappop(q2)
            else:
                while q1 and not visited[q1[0][1]]:
                    heapq.heappop(q1)
                if q1:
                    visited[q1[0][1]] = False
                    heapq.heappop(q1)

    while q1 and not visited[q1[0][1]]:
        heapq.heappop(q1)
    while q2 and not visited[q2[0][1]]:
        heapq.heappop(q2)

    if not q1 or not q2:
        print("EMPTY")
    else:
        a = -q2[0][0]
        b = q1[0][0]
        print("%d %d" % (a, b))
