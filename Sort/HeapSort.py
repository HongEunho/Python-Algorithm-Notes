heap = [7, 6, 5, 8, 3, 5, 9, 1, 6]
number = 9

for i in range(1, number):
    c = i
    while c != 0:
        root = int((c - 1) / 2)
        if heap[root] < heap[c]:
            heap[root], heap[c] = heap[c], heap[root]

        c = root

for i in range(number-1, -1, -1):
    heap[0], heap[i] = heap[i], heap[0]

    root = 0
    c = 1
    while c < i:
        c = 2 * root + 1
        if c < i - 1 and heap[c] < heap[c+1]:
            c += 1

        if c < i and heap[root] < heap[c] :
            heap[root], heap[c] = heap[c], heap[root]

        root = c


for i in range(number):
    print(heap[i], end = ' ')