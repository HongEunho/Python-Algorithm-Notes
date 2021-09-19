n = int(input())
graph = []
answer = []


def recursive(x, y, N):
    answer.append("(")
    for i in range(2):
        for j in range(2):
            count0, count1 = 0, 0
            tmpGraph = []
            for k in range(N):
                tmpGraph.append(graph[x + i * N + k][y + j * N:y + (j + 1) * N])
                if '0' in tmpGraph[k]:
                    count0 = 1
                if '1' in tmpGraph[k]:
                    count1 = 1

            if count0 == 1:
                if count1 == 1:
                    recursive(x + i * N, y + j * N, int(N / 2))
                else:
                    answer.append(0)
            elif count1 == 1:
                answer.append(1)

    answer.append(")")


contain0 = 0
contain1 = 0
for i in range(n):
    graph.append(list(input()))
    if '0' in graph[i]:
        contain0 = 1
    if '1' in graph[i]:
        contain1 = 1


if contain0 == contain1:
    recursive(0, 0, int(n / 2))
    for i in answer:
        print(i, end='')

else:
    if contain0 == 1:
        print(0)
    else:
        print(1)
