n, m = map(int, input().split())

answer = []


def dfs(a):
    if a == 0:
        print(" ".join(map(str, answer)))
        return

    for i in range(1, n + 1):
        answer.append(i)
        dfs(a - 1)
        answer.pop()


dfs(m)
