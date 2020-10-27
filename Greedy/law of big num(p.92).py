N,M,K = map(int,input().split())

a = list(map(int,input().split()))

a.sort()

mostbig = a[-1]
secbig = a[-2]

result = 0
count = 0

for i in range(M):
    if count != K:
        result += mostbig
        count += 1
    else:
        count = 0
        result += secbig

print(result)