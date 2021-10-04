def solution(n, k, cmd):
    OX = ["0" for _ in range(n)]
    up = []
    down = []
    delete = []

    for i in range(n):
        if i < k:
