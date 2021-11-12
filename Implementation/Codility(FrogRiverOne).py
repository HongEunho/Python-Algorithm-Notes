from collections import deque

def solution(X, A):
    check = [0] * X
    mysum = 0

    for idx, i in enumerate(A):
        if check[i-1] == 0:
            check[i-1] = 1
            mysum += 1
            if mysum == X:
                return idx

    return -1