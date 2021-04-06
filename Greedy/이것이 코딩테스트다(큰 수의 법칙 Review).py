n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
first = arr[-1]
second = arr[-2]

answer = 0

while True:
    for i in range(k):
        if m == 0:
            break
        answer += first
        m -= 1
    if m == 0:
        break
    answer += second
    m -= 1

print(answer)