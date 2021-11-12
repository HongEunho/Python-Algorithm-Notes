def solution(A):
    front = A[0]
    back = sum(A[1:])
    min_result = abs(front-back)
    for i in range(1, len(A)-1):
        front += A[i]
        back -= A[i]
        result = abs(front-back)
        if min_result > result:
            min_result = result
    return min_result