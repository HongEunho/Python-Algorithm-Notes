n = int(input())

graph = [[" "]*(2*n-1) for _ in range(n)]
def recursive(N, before):
    for i in range(2*N):
        