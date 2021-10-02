n = list(input())

n = list(map(int, n))
n.sort(reverse=True)

for i in n:
    print(i, end='')