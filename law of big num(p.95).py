N, M, K = map(int,input().split())
a = list(map(int,input().split()))

a.sort()
most = a[-1]
second = a[-2]

result = 0

count = M // (K+1) * K
count += M%(K+1)

result += count * most
result += (M-count)*second

print(result)