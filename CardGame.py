# 입력은 N*M의 행렬을 입력받는 것이 끝.
# 문제는 어떤 행을 뽑았을 때 그 행에서의 가장 작은 수가 다른 행의 가장 작은 수 보다 커야 하는 카드게임이다.
# 이렇게 게임을 진행했을 때 나오는 수를 출력하는 것이다.
# 즉 해당 라인중에서 가장 낮은 수를 뽑았을 때 그 수가 다른 행에서 같은 방식을 진행했을 때 보다 큰 수가 되어야 하는 문제

n,m = map(int,input().split())

a = [[0]*n]*m
tmp = [0]*n
# a = [[0 for col in range(11)] for row in range(10)]

for i in range(n):
    a[i] = input().split()
    a[i].sort()
    tmp[i] = a[i][0]
print(max(tmp))