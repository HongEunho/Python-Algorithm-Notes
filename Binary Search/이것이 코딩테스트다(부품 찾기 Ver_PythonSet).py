n = int(input())
array = set(map(int, input().split()))

m = int(input())
guest = list(map(int, input().split()))

for i in guest:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')