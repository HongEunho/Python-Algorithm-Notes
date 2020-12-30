from collections import deque

def BFS(graph, start):
    queue = deque([start]) #큐에 넣어주고
    visited[start] = True #방문처리
    while queue: #큐가 빌 때 까지
        v = queue.popleft()
        print(v, end='') #먼저 넣은 원소부터 뽑아 출력
        for i in graph[v]: #해당 원소와 연결된 그래프 확인 후 방문X면 큐에 삽입
            if not visited[i]:
                queue.append(i)
                visited[i]=True



graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9
BFS(graph, 1)