dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(graph, price, x, y, fx, fy, n):

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if graph[nx][ny] == 1:
            continue
            
        if fx!=nx and fy!= ny:
            if price[x][y]+600 < price[nx][ny]:
                a = price[nx][ny]
                price[nx][ny] = price[x][y]+600
                dfs(graph, price, nx, ny, x, y, n)
                if nx != n-1 and ny != n-1:
                    price[nx][ny] = a
        else:
            if price[x][y]+100 < price[nx][ny]:
                a = price[nx][ny]
                price[nx][ny] = price[x][y]+100
                dfs(graph, price, nx, ny, x, y, n)
                if nx != n - 1 and ny != n - 1:
                    price[nx][ny] = a

def solution(board):
    answer = 0
    n = len(board)
    price = [[int(1e9)]*n for _ in range(n)]
    price[0][0] = 0
    dfs(board, price, 0, 0, 0, 0, n)
    answer = price[n-1][n-1]

    return answer

print(solution([[0, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 1, 1, 1, 1],
[1, 1, 1, 1, 0, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 1, 1, 1, 1],
[0, 1, 0, 1, 1, 1, 1, 1, 1],
[0, 1, 0, 0, 0, 1, 1, 1, 1],
[0, 1, 1, 1, 0, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 1, 1, 1, 1],
[1, 1, 1, 1, 0, 0, 0, 0, 0]]))
