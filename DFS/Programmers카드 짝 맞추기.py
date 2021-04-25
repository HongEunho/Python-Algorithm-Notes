def dfs(board, r, c, cnt):
    if r<0 or r>3 or c<0 or c>3:
        return False

    ctleft, ctright, ctup, ctdown = 0, 0, 0, 0
    for i in range(c+1, 4):
        if r >
        if board[r][i]

    dx = [0,0,1,-1,0,0,ctdown,ctup]
    dy = [1,-1,0,0,ctright,ctleft,0,0]

    for i in range(8):



def solution(board, r, c):
    answer = 0
    cnt = 0
    dfs(board, r, c, cnt)


    return answer

print(solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0))