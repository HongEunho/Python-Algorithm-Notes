def solution(new_id):
    answer = ''
    answer += new_id

    answer = answer.lower()
    answer2 = ''
    for i in answer:
        if i.islower() or i.isdigit() or i=='-' or i=='_' or i=='.':
            answer2 += i

    while ".." in answer2:
        answer2= answer2.replace("..", ".")

    answer4 = list(answer2)
    if answer4[0] == '.':
        del answer4[0]
    if len(answer4)>0:
        if answer4[-1] == '.':
            del answer4[-1]

    if len(answer4) == 0:
        answer4.append('a')

    if len(answer4) >= 16:
        answer4 = answer4[:15]
        if answer4[-1] == '.':
            answer4 = answer4[:-1]

    if len(answer4) <= 2:
        while len(answer4) < 3:
            answer4 += answer4[-1]



    return "".join(answer4)

print(solution("...!@BaT#*..y.abcdefghijklm"))