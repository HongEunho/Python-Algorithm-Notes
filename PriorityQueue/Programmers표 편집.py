import heapq


def solution(n, k, cmd):
    answer = ''
    left, right, delete = [], [], []
    result = []

    for i in range(n):
        heapq.heappush(right, i)

    for i in range(k):
        heapq.heappush(left, -heapq.heappop(right))

    for i in cmd:
        if len(i) > 1:
            tmp = i.split()

            if tmp[0] == 'D':
                for j in range(int(tmp[1])):
                    if right:
                        heapq.heappush(left, -heapq.heappop(right))

            elif tmp[0] == 'U':
                for j in range(int(tmp[1])):
                    if left:
                        heapq.heappush(right, -heapq.heappop(left))

        elif i == 'C':
            delete.append(heapq.heappop(right))

            if not right:
                heapq.heappush(right, -heapq.heappop(left))

        elif i == 'Z':
            z = delete.pop()

            if z < right[0]:
                heapq.heappush(left, -z)
            else:
                heapq.heappush(right, z)

    while left:
        result.append(-heapq.heappop(left))

    while right:
        result.append(heapq.heappop(right))

    for i in range(n):
        if i in result:
            answer += "O"
        else:
            answer += "X"

    return answer

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))