import heapq

n = int(input())

queue = []
myList = []
for i in range(n):
    heapq.heappush(queue, int(input()))
    myList.append(heapq.heappop(queue))
    
    print(queue)
    length = len(queue)
    if length % 2 == 0:
        print(queue[length//2 - 1])
    else:
        print(queue[length//2])
