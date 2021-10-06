n, m = map(int, input().split())
answer = []


def dfs(start, a):
    if a == 0:
        print(" ".join(map(str, answer)))
        return

    for i in range(start, n + 1):
        if i >= start:
            answer.append(i)
            dfs(i, a - 1)
            answer.pop()


dfs(1, m)
