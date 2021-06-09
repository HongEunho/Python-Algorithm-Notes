def solution(places):
    answer = []
    # dx = [0,1,1,1,0,-1,-1,-1,0,2,0,-2]
    # dy = [1,1,0,-1,-1,-1,0,1,2,0,-2,0]
    dx = [0,1,-1]
    dy = [1,0,0]
    dx2 = [-1,1]
    dy2 = [1,1]
    dx3 = [0,2,-2]
    dy3 = [2,0,0]

    length = len(places)
    for i in range(5):
        flag = 0
        for j in range(5):
            for k in range(5):
                if places[i][j][k]=='P':
                    tmp = []

                    for z in range(3): #동남북
                        nx = j + dx[z]
                        ny = k + dy[z]
                        if nx<0 or nx>=5 or ny<0 or ny>=5:
                            continue

                        if places[i][nx][ny]=='P':
                            flag = 1
                            answer.append(0)
                            print("%d %d %d"%(i,j,k))
                            break

                        if places[i][nx][ny]=='X':
                            tmp.append(z) # 파티션 있는 방향 저장

                    if flag == 1:
                        break

                    for z in range(2): # 대각선
                        nx = j + dx2[z]
                        ny = k + dy2[z]
                        if nx<0 or nx>=5 or ny<0 or ny>=5:
                            continue
                        if places[i][nx][ny] == "P":
                            if z == 0:
                                if not(0 in tmp and 2 in tmp):
                                    flag = 1
                                    answer.append(0)
                                    print("%d %d %d" % (i, j, k))
                                    print(tmp)
                                    break
                            elif z == 1:
                                if not(0 in tmp and 1 in tmp):
                                    flag = 1
                                    answer.append(0)
                                    break

                    if flag == 1:
                        break

                    for z in range(3): #두배 동남북
                        nx = j + dx3[z]
                        ny = k + dy3[z]
                        if nx<0 or nx >= 5 or ny < 0 or ny >= 5:
                            continue
                        if places[i][nx][ny] == "P":
                            if z not in tmp:
                                flag = 1
                                answer.append(0)
                                break


                if flag == 1: # k범위
                    break

            if flag == 1: # j범위
                break

        if flag == 0:
            answer.append(1)

    return answer

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))