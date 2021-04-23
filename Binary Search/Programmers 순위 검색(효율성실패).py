from itertools import combinations


def solution(info, query):
    answer = [0 for i in range(len(query))]
    mydict = {}
    infol = []
    queryl = []
    for i in range(len(info)):
        infol.append(info[i].split())
        # tmp = ['java', 'backend', 'junior', 'pizza', '150']
    for j in range(len(query)):
        queryl.append(query[j].split())
        while len(queryl[j]) > 5:
            queryl[j].remove("and")

    for i in range(len(infol)):
        for j in range(len(queryl)):
            flag = 0
            for k in range(4):
                if infol[i][k] != queryl[j][k]:
                    if queryl[j][k] != '-':
                        flag = 1
                        break
            if flag == 0:
                if int(infol[i][4]) >= int(queryl[j][4]):
                    answer[j] += 1

    return answer