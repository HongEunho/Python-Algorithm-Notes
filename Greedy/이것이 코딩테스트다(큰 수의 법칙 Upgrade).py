n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
first = arr[-1]
second = arr[-2]

count = m//(k + 1) * k
count += m % (k + 1)

answer = count*first
answer += (m-count)*second

print(answer)