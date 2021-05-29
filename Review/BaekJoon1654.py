k, n = map(int, input().split())
lan = []

def binary_search(target, start, end):
    while start <= end:
        lines = 0
        mid = (start+end) // 2

        for i in lan:
            lines += i // mid

        if lines < target:
            end = mid - 1
        else:
            start = mid + 1

    return end

for i in range(k):
    lan.append(int(input()))

maxlan = max(lan)

result = binary_search(n, 1, maxlan)
print(result)