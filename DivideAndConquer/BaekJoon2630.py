n = int(input())


def recursive(x, y, N):
    flag = False

    for i in range(x, x + N):
        if flag:
            break

        for j in range(y, y + N):
            if graph[x][y] != graph[i][j]:
                recursive(x, y, N // 2)
                recursive(x, y + N // 2, N // 2)
                recursive(x + N // 2, y, N // 2)
                recursive(x + N // 2, y + N // 2, N // 2)

                flag = True
                break

    if not flag:
        if graph[x][y] == 0:
            count[0] += 1
        else:
            count[1] += 1


graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

count = [0, 0]

recursive(0, 0, n)
for i in count:
    print(i)