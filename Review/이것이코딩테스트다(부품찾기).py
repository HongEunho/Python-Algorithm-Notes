import sys

n = int(sys.stdin.readline().rstrip())
allItems = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
findItems = list(map(int, sys.stdin.readline().rstrip().split()))

allItems.sort()


def findItem(target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if allItems[mid] == target:
            return mid

        elif allItems[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


for i in findItems:
    result = findItem(i, 0, n - 1)
    if result is not None:
        print("yes", end=' ')
    else:
        print("no", end=' ')
