from itertools import product

n = int(input())
num = list(map(int, input().split()))
mark = list(map(int, input().split()))

maxResult = int(-1e9)
minResult = int(1e9)


def dfs(index, result):
    global maxResult, minResult
    if index == n:
        maxResult = max(maxResult, result)
        minResult = min(minResult, result)

        return

    for i in range(4):
        if not mark[i] == 0:
            if i == 0:
                tmp = result + num[index]
            elif i == 1:
                tmp = result - num[index]
            elif i == 2:
                tmp = result * num[index]
            else:
                tmp = int(result/num[index])

            mark[i] -= 1
            dfs(index + 1, tmp)
            mark[i] += 1


dfs(1, num[0])

print(maxResult)
print(minResult)
