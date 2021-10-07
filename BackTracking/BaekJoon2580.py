import sys
graph = []

for i in range(9):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

def checkCol(x, col):
    for i in range(9):
        if x == graph[i][col]:
            return False
    return True


def dfs():

    for i in range(9):
        

        