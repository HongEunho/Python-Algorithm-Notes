def solution(new_id):
    answer = ''
    #step1
    answer1 = new_id.lower()

    #step2
    answer2 = ''
    for i in answer1:
        if i.islower() or i.isdigit() or i == '-' or i == '_' or i == '.':
            answer2 += i

    #step3
    answer3=''
    for i in range(0, len(answer2)):
        if i and answer2[i] == '.' and answer2[i-1] == '.':
            continue
        answer3 += answer2[i]

    #step4
    answer4=''
    for i in range(len(answer3)):
        if i == 0 and answer3[i] == '.':
            continue
        if i == len(answer3)-1 and answer3[i] == '.':
            continue
        answer4 += answer3[i]

    #step5
    answer5 = ''
    if len(answer4) == 0:
        answer5+='a'
    else:
        answer5 = answer4

    #step6
    answer6 = ''
    if len(answer5) >= 16:
        answer6 = answer5[:14]
        if answer5[14] != '.':
            answer6 += answer5[14]
    else:
        answer6 = answer5

    #step7
    if len(answer6) <= 2:
        while len(answer6) < 3 :
            answer6 += answer6[-1]

    return answer6

print(solution("=.="))

