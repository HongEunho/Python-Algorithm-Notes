n, m = map(int, input().split())
alist = list(map(int, input().split()))

start = 0
end = 0
count = 0

while end < len(alist) and start < len(alist):
    if sum(alist[start:end+1]) < m:
        end += 1

    elif sum(alist[start:end+1]) == m:
        count += 1
        if start < end:
            start += 1
        else:
            end += 1

    else:
        start += 1

print(count)