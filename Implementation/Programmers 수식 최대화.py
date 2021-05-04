from itertools import permutations

def solution(expression):
    answer = 0
    oper = ["*", "+", "-"]
    mymax = int(-1e9)

    for per in permutations(oper, 3):
        perm = list(per)
        exp = ''
        tmp = []
        for i in range(len(expression)):
            if str(0) <= expression[i] <= str(9):
                exp += expression[i]
            else:
                tmp.append(exp)
                tmp.append(expression[i])
                exp = ''
            if i == len(expression) - 1:
                tmp.append(exp)


        for j in range(len(perm)):
            i = 0
            while i < len(tmp):
                if tmp[i] == perm[j]:
                    tmp[i-1] = eval(str(tmp[i-1])+perm[j]+str(tmp[i+1]))
                    del tmp[i]
                    if i < len(tmp):
                        del tmp[i]
                else:
                    i+=1

        mymax = max(mymax, abs(tmp[0]))
        
    return mymax

print(solution("100-200*300-500+20"))