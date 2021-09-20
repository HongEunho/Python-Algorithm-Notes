n, r, c = map(int, input().split())
num = -1


def recursive(x, y, N):
    global num

    if N == 2:
        for i in range(x, x + N):
            for j in range(y, y + N):
                num += 1
                if i == r and j == c:
                    print(num)
                    exit(0)
        return

    if not (x <= r < x + N and y <= c < y + N):
        num += N * N
        return

    for i in range(x, x + N, N // 2):
        for j in range(y, y + N, N // 2):
            recursive(i, j, N // 2)


recursive(0, 0, 2 ** n)

