import math
t = int(input())

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = math.sqrt((x1 - x2)**2 + (y1-y2)**2)

    if x1 == x2 and y1 == y2:   # 두 원의 중심이 같을 때
        if r1 == r2:            # 반지름이 같으면 : 같은 원
            print(-1)
        else:
            print(0)            # 다르면 영원히 만나지 않음

    else:                       # 두 원의 중심이 다를 때
        if abs(r1-r2) == dist or r1 + r2 == dist: # 내접원 or 외접원
            print(1)
        elif abs(r1-r2) < dist < r1 + r2:   # 두 점에서 만날 때
            print(2)
        else:           # 만나지 않음
            print(0)

