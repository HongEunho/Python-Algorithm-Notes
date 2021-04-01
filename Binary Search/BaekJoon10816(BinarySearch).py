from sys import stdin
n = stdin.readline().rstrip()
card = list(map(int,stdin.readline().split()))
m = stdin.readline().rstrip()
test = list(map(int,stdin.readline().split()))

card.sort()

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return array[start:end+1].count(target)
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)

for i in range(len(test)):
    a = binary_search(card, test[i], 0, len(card)-1)
    if a is not None:
        print(a, end=' ')
    else:
        print(0, end=' ')