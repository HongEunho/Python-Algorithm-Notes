import copy
r, c = map(int, input().split())

graph = []
for i in range(r):
    graph.append(list(input()))
new_graph = copy.deepcopy(graph)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for x in range(r):
    for y in range(c):
        if graph[x][y] == '.':
            continue
        sea_count = 0
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                sea_count += 1
                continue
            elif graph[nx][ny] == '.':
                sea_count += 1

        if sea_count >= 3:
            new_graph[x][y] = '.'

start_row = 0
start_col = 0
end_row = 0
end_col = 0
min_index = c-1
max_index = 0

for i in range(r):
    if 'X' in new_graph[i]:
        start_row = i
        break

for i in range(r-1, -1, -1):
    if 'X' in new_graph[i]:
        end_row = i
        break

for i in range(start_row,  end_row+1):
    tmp = [i for i, value in enumerate(new_graph[i]) if value == 'X']
    if not tmp:
        continue
    min_tmp = tmp[0]
    max_tmp = tmp[-1]
    min_index = min(min_index, min_tmp)
    max_index = max(max_index, max_tmp)

for i in range(start_row, end_row+1):
    for j in range(min_index, max_index+1):
        print(new_graph[i][j], end='')
    print()
