def turn(idx, dir):
    if dir == 1:  # 시계
        wheel[idx][0], wheel[idx][1], wheel[idx][2], wheel[idx][3], wheel[idx][4], wheel[idx][5], wheel[idx][6], \
        wheel[idx][7] = \
            wheel[idx][7], wheel[idx][0], wheel[idx][1], wheel[idx][2], wheel[idx][3], wheel[idx][4], wheel[idx][5], \
            wheel[idx][6]
    else:  # 반시계
        wheel[idx][0], wheel[idx][1], wheel[idx][2], wheel[idx][3], wheel[idx][4], wheel[idx][5], wheel[idx][6], \
        wheel[idx][7] = \
            wheel[idx][1], wheel[idx][2], wheel[idx][3], wheel[idx][4], wheel[idx][5], wheel[idx][6], wheel[idx][7], \
            wheel[idx][0]


def solve(idx, dir):
    if idx == 0:
        if wheel[0][2] == wheel[1][6]:
            turn(0, dir)  # 0번만 턴
        else:
            if wheel[1][2] == wheel[2][6]:  # 0, 1번 턴
                turn(0, dir)
                turn(1, -dir)
            else:
                if wheel[2][2] == wheel[3][6]:  # 0, 1, 2번 턴
                    turn(0, dir)
                    turn(1, -dir)
                    turn(2, dir)
                else:  # 모두 다르기 때문에 턴
                    turn(0, dir)
                    turn(1, -dir)
                    turn(2, dir)
                    turn(3, -dir)

    elif idx == 1:
        if wheel[1][2] == wheel[2][6]:  # 1, 2번 톱니 같을 때
            if wheel[1][6] == wheel[0][2]:  # 0, 1번 톱니도 같으면
                turn(1, dir)  # 1번만 회전
            else:  # 0,1 은 다르면
                turn(1, dir)
                turn(0, -dir)

        else:  # 1, 2번 톱니 다를 때
            if wheel[1][6] == wheel[0][2]:  # 0, 1번 톱니는 같다면
                if wheel[2][2] == wheel[3][6]:
                    turn(1, dir)
                    turn(2, -dir)
                else:
                    turn(1, dir)
                    turn(2, -dir)
                    turn(3, dir)
            else:  # 0, 1번 톱니도 다르면
                if wheel[2][2] == wheel[3][6]:  # 2, 3번 톱니는 같다면
                    turn(0, -dir)
                    turn(1, dir)
                    turn(2, -dir)
                else:
                    turn(0, -dir)
                    turn(1, dir)
                    turn(2, -dir)
                    turn(3, dir)

    elif idx == 2:
        if wheel[2][6] == wheel[1][2]:  # 1, 2번 톱니 같을 때
            if wheel[2][2] == wheel[3][6]:  # 2, 3번 톱니도 같으면
                turn(2, dir)  # 2번만 회전
            else:  # 2, 3은 다르면
                turn(2, dir)
                turn(3, -dir)

        else:  # 1, 2번 톱니 다를 때
            if wheel[3][6] == wheel[2][2]:  # 2, 3번 톱니는 같다면
                if wheel[0][2] == wheel[1][6]:
                    turn(2, dir)
                    turn(1, -dir)
                else:
                    turn(0, dir)
                    turn(1, -dir)
                    turn(2, dir)
            else:  # 2, 3번 톱니도 다르면
                if wheel[0][2] == wheel[1][6]:  # 0, 1번 톱니는 같다면
                    turn(1, -dir)
                    turn(2, dir)
                    turn(3, -dir)
                else:
                    turn(0, dir)
                    turn(1, -dir)
                    turn(2, dir)
                    turn(3, -dir)

    else:
        if wheel[3][6] == wheel[2][2]:
            turn(3, dir)
        else:
            if wheel[1][2] == wheel[2][6]:
                turn(3, dir)
                turn(2, -dir)
            else:
                if wheel[1][6] == wheel[0][2]:
                    turn(3, dir)
                    turn(2, -dir)
                    turn(1, dir)
                else:
                    turn(3, dir)
                    turn(2, -dir)
                    turn(1, dir)
                    turn(0, -dir)


wheel = []
for i in range(4):
    wheel.append(list(map(int, input())))

k = int(input())
for i in range(k):
    a, b = map(int, input().split())
    solve(a - 1, b)

answer = 0
for i in range(4):
    if wheel[i][0] == 0:
        answer += 0
    else:
        answer += 2 ** i

print(answer)
