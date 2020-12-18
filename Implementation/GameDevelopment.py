x, y = map(int,input().split())
pos_row, pos_col, pos_dir = map(int,input().split())

visit = [[0]*y for _ in range(x)]
visit[pos_row][pos_col] = 1

array = []
for i in range(x):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global pos_dir
    pos_dir -= 1
    if pos_dir == -1:
        pos_dir = 3

count = 1
turn_count = 0

while True:
    turn_left()
    nx = pos_row + dx[pos_dir]
    ny = pos_col + dy[pos_dir]

    if visit[nx][ny] == 0 and array[nx][ny] == 0:
        visit[nx][ny] = 1
        pos_row = nx
        pos_col = ny
        count += 1
        turn_count = 0
        continue

    else:
        turn_count += 1
    if turn_count == 4:
        nx = pos_row - dx[pos_dir]
        ny = pos_col - dy[pos_dir]

        if array[nx][ny] == 0:
            pos_row = nx
            pos_col = ny
        else:
            break
        turn_count = 0

print(count)