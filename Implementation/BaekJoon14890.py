n, l = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

answer = 0


def solve(arr):
    cnt = 1
    flag = True
    pre_high = False

    for i in range(n - 1):
        if arr[i] == arr[i + 1]:
            cnt += 1
            if pre_high:
                if cnt >= l:
                    cnt = 0
                    pre_high = False
                    flag = True
                else:
                    flag = False

        elif arr[i] > arr[i + 1]:
            if arr[i] - arr[i + 1] > 1:
                flag = False
                break

            if pre_high:
                if cnt < l:
                    flag = False
                    break
                pre_high = False
            else:
                pre_high = True
            cnt = 1
            if cnt < l:
                flag = False
            elif cnt == l:
                pre_high = False
                cnt = 0

        else:
            if arr[i + 1] - arr[i] > 1:
                flag = False
                break

            if cnt < l:
                flag = False
                break
            cnt = 1
            pre_high = False

    if flag:
        return True
    return False

for i in range(n):
    if solve(graph[i]):
        answer += 1
    if solve([arr[i] for arr in graph]):
        answer += 1

print(answer)
