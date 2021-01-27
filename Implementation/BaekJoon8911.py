n = int(input())

dx = [0,-1,0,1]
dy = [1,0,-1,0] # 북 서 남 동

for i in range(n):
    pos_x = 0
    pos_y = 0
    pos_dir = 0  # 0북 1서 2남 3동
    move = list(input())
    trace = [(pos_x, pos_y)]
    for j in move:
        if j == 'F':
            pos_x = pos_x + dx[pos_dir]
            pos_y = pos_y + dy[pos_dir]
        elif j == 'B':
            pos_x = pos_x - dx[pos_dir]
            pos_y = pos_y - dy[pos_dir]
        elif j == 'L':
            if pos_dir == 3:
                pos_dir = 0
            else:
                pos_dir += 1
        elif j == 'R':
            if pos_dir == 0:
                pos_dir = 3
            else:
                pos_dir -= 1

        trace.append((pos_x, pos_y))
    width = max(trace, key = lambda x:x[0])[0] - min(trace, key = lambda x:x[0])[0]
    height = max(trace, key = lambda x:x[1])[1] - min(trace, key = lambda x:x[1])[1]
    print(width * height)


