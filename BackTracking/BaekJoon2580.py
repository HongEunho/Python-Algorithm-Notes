import sys
graph = []

for i in range(9):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

def dfs():

    for i in range(9):
        