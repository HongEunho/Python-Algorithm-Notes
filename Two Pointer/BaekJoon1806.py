import sys
n, s = map(int, sys.stdin.readline().split())
nlist = list(map(int, sys.stdin.readline().split()))

start, end = 0, 0
flag = 0
shortest = n
count = 0
mysum = nlist[0]

while end < n:

    if mysum < s:   # 현재 구간합이 s보다 작으면
        end += 1    # 현재 구간의 끝점을 늘려준다
        if end < n: # 끝이 n을 벗어나면 안되기 때문에 범위 고려
            mysum += nlist[end]

    else:           # 현재 구간합이 s보다 크거나 같을 경우
        flag = 1    # 답을 찾을 수 있다는 표시
        if shortest > end-start:    # 현재까지의 최소거리보다 짧으면
            shortest = end-start+1  # 최소거리 갱신

        if start < end:             # 구간 시작점이 끝점보다 앞에있으면
            mysum -= nlist[start]   # 구간 시작점을 하나 늘린다
            start += 1
        else:                       # 구간 시작점이 끝점과 같거나 뒤에있으면
            end += 1                # 구간 끝점을 하나 뒤로 늘려서 end가 start뒤에 오도록 유지
            if end < n:
                mysum += nlist[end] # 끝점을 늘려가며 부분합 추가

if flag==1:
    print(shortest)
else:
    print(0)