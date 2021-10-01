t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    dist = y - x
    step = 1        # 이동할 거리(초기는 1)
    cnt = 0         # 횟수 별 카운트 변수
    mydist = 0      # 초기 이동거리는 0

    while mydist < dist:
        cnt += 1
        mydist += step

        if cnt % 2 == 0:
            step += 1

    print(cnt)