n, m = map(int, input().split())

before = []
after = []

dx = [0, 0, 0, 1, 1, 1, 2, 2, 2]
dy = [0, 1, 2, 0, 1, 2, 0, 1, 2]

for i in range(n):
    before.append(list(map(int, input())))

for i in range(n):
    after.append(list(map(int, input())))


def solution(result):
    for x in range(n - 2):
        for y in range(m - 2):

            if before[x][y] != after[x][y]:
                result += 1
                for i in range(9):
                    before[x + dx[i]][y + dy[i]] = 1 - before[x + dx[i]][y + dy[i]]

            if before == after:
                print(result)
                return

            else:
                if x == n - 3 and y == m - 3:
                    print(-1)
                    return


if before == after:
    print(0)
else:
    solution(0)
