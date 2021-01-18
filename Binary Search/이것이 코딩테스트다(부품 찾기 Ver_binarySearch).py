import sys


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)


n = int(input())
array = list(map(int, sys.stdin.readline().split()))

m = int(input())
guest = list(map(int, sys.stdin.readline().split()))

array.sort()

for target in guest:
    result = binary_search(array, target, 0, n - 1)

    if result is not None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
