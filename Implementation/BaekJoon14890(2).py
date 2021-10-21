n, l = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

answer = 0

def solve(arr):
    load = [False]*n
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            continue
        if abs(arr[i] - arr[i+1]) > 1:
            return False
        if arr[i] > arr[i+1]:
            tmp = arr[i+1]
            for j in range(i+1, i+1+l):
                if j < n:
                    if arr[j] != tmp:
                        return False
                    if load[j]:
                        return False
                    load[j] = True
                else:
                    return False
        else:
            tmp = arr[i]
            for j in range(i, i-l, -1):
                if 0 <= j:
                    if arr[j] != tmp:
                        return False
                    if load[j]:
                        return False
                    load[j] = True
                else:
                    return False
    return True

for i in range(n):
    if solve(graph[i]):
        answer += 1
    if solve([arr[i] for arr in graph]):
        answer += 1

print(answer)