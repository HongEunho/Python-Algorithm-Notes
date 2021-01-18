import sys

n = int(input())
array = list(map(int, sys.stdin.readline().split()))

store_max = max(array) # 현재 가게에 존재하는 부품번호의 최댓값
count_array = [0]*(store_max+1)

m = int(input())
guest = list(map(int, sys.stdin.readline().split()))

for i in range(len(array)):
    count_array[array[i]] += 1

for i in guest:
    if i > store_max or count_array[i] == 0:
        print('no', end=' ')
    else:
        print('yes', end=' ')