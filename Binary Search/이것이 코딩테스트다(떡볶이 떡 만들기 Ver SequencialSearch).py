n, m = map(int, input().split())


def cut_dduck(a):
    if a <= i:
        return 0
    else:
        return a - i


dduck = list(map(int, input().split()))
max_dduck = max(dduck)
answer = 0

for i in range(max_dduck):
    rest = list(map(cut_dduck, dduck))
    print(rest)
    if sum(rest) >= m:
        answer = max(answer, i)

print(answer)