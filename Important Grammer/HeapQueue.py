import heapq
# 보통 다익스트라 최단 경로 알고리즘을 포함한 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용
# PriorityQueue도 있지만 보통 heapq가 더 빠름

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
