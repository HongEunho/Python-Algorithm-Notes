from itertools import combinations


def solution(info, query):
    answer = [0 for i in range(len(query))]
    mydict = {}
    infol = []
    queryl = []
    for i in range(len(info)):
        infol.append(info[i].split())
        # tmp = ['java', 'backend', 'junior', 'pizza', '150']
        print(infol)
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
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
               ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))