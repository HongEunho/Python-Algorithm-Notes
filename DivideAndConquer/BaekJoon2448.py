n = int(input())

graph = [[" ", " ", "*", " ", " "], [" ", "*", " ", "*", " "], ["*", "*", "*", "*", "*"]]


def recursive(N, before):
    after = [[" "] * (2 * 2 * N - 1) for _ in range(2 * N)]
    for i in range(N):
        after[i][N:N+2*N-1] = before[i]

    k = 0
    for i in range(N, 2 * N):
        after[i][:2*N] = before[k]
        after[i][2 * N:2 * N+len(before[k])] = before[k]
        k += 1

    if 2 * N == n:
        return after

    return recursive(2 * N, after)


if n == 3:
    result = graph
else:
    result = recursive(3, graph)

for i in result:
    print("".join(i))
