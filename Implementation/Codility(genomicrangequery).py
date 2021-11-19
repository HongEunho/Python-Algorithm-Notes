def solution(S, P, Q):
    arr = []
    for i in range(len(P)):
        A = P[i]
        B = Q[i]
        min_num = 5

        if 'A' in S[A:B+1]:
            num = 1
        elif 'C' in S[A:B+1]:
            num = 2
        elif 'G' in S[A:B+1]:
            num = 3
        else:
            num = 4
        if min_num > num:
            min_num = num
        arr.append(min_num)
    return arr
