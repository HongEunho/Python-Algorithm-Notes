n = int(input())

score = []
for i in range(n):
    score.append(int(input()))

result = 0
for i in range(n-1, 0, -1):
    if score[i] <= score[i-1]:
        tmp = score[i]-1
        result += (score[i-1] - tmp)
        score[i-1] = score[i]-1

print(result)